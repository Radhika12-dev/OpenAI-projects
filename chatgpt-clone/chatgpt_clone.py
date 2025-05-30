import os
import openai
import time
import json
import streamlit as st
from utils import load_openai_key
from constants import *

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding='utf-8') as f:
            history =  json.load(f)
        #Filter out the older history
        now = time.time()
        filtered = [
            q for q in history if now- q["timestamp"] < HISTORY_EXPIRY_DAYS * 24 * 60 * 60
        ]
        #Save the filtered history to cleanu
        save_history(filtered)
        return filtered

    return []

def save_history(history):
    with open(HISTORY_FILE, "w", encoding='utf-8') as f:
        json.dump(history, f)

def gpt_clone(messages, cache):
    conversation_key = tuple((msg['role'], msg['content']) for msg in messages)
    if conversation_key in cache:
        return cache[conversation_key]
    try:
        response = openai.chat.completions.create(
            model="gpt-4.1-nano",
            messages=messages,
            temperature=0.7,
            max_tokens=300
        )
        bot_response = response.choices[0].message.content
    except Exception as e:
        bot_response = f"Error: {e}"
        
    cache[conversation_key] = bot_response
    return bot_response

if __name__ == "__main__":
    openai.api_key = load_openai_key()
    st.set_page_config(page_title="Helping Agent", page_icon=":robot_face:", layout="wide")
        # Custom CSS for vertical divider and history background
    st.markdown("""
    <style>
    .vertical-divider {
        border-left: 2px solid #bbb;
        height: 100vh;
        position: absolute;
        left: 100%;
        top: 0;
    }
    .history-col {
        
        border-radius: 8px;
        padding: 13px 14px 18px 18px;
        min-height: 400px;
    }
    .header-small {
        font-size: 1.5rem !important;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant. Answer the user's questions to the best of your ability. Always ask a following question to the user."}
        ]
    
    if "user_questions" not in st.session_state:
        st.session_state.user_questions = load_history()
    
    if "cache" not in st.session_state:
        st.session_state.cache = {}

    # Page header
    st.markdown('<div style="text-align:center;"><span class="header-small">Helping Agent</span></div>', unsafe_allow_html=True)
    st.write("")  # spacing

    #Layout: left for questions, center for chat input/output
    col1, col2 = st.columns([0.25, 0.75], gap="small")

    with col1:
         # Add a placeholder for the input box to update from history
        input_placeholder = st.empty()
        st.subheader("Previously asked...", divider="gray")
        if st.session_state.user_questions:
            for i, q in enumerate(st.session_state.user_questions, 1):
                question_text = q["question"]
                if st.button(f"{i}. {question_text}", key=f"history_{i}"):
                    st.session_state.selected_history = question_text
        else:
            st.write("No questions asked yet.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.subheader("Ask a Question")
        #Use session_state to prefill the input if a history question was clicked.
        default_input = st.session_state.get("selected_history", "")
        with st.form(key="chat_form", clear_on_submit=True):
            user_input = st.text_input("Type your question here:", value=default_input)
            submit_button = st.form_submit_button("Send")

        # Update session_state.input_value after form submit or history click
        st.session_state.input_value = user_input

        if submit_button and user_input.strip():
            #Add user question to history
            st.session_state.messages.append({'role': 'user', 'content': user_input})

            #Prevent duplicate questions in history
            if user_input not in st.session_state.user_questions:
                if not any(q["question"] == user_input for q in st.session_state.user_questions):
                    st.session_state.user_questions.append({
                        "question": user_input,
                        "timestamp": time.time()
                    })
                    save_history(st.session_state.user_questions)

            #Clear selected history after submission
            if "selected_history" in st.session_state:
                del st.session_state.selected_history

            #Call OpenAI API
            bot_response = gpt_clone(st.session_state.messages, st.session_state.cache)
            st.session_state.messages.append({'role': 'assistant', 'content': bot_response})
            st.session_state.input_value = ""  # Clear input after sending
        
        #Display conversation
        for idx, msg in enumerate(st.session_state.messages[1:]):  # Skip the system message
            if msg['role'] == 'user':
                st.markdown(
                    f"""
                    <div style='padding:10px 16px; border-radius:12px; margin-bottom:8px; text-align:right;'>
                        <b>You:</b> {msg['content']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style='background-color:#F5F5F5; color:#111; padding:10px 16px; border-radius:12px; margin-bottom:8px; text-align:left;'>
                        <b>Bot:</b> {msg['content']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                 # feedback buttons
                fb_col1, fb_col2, fb_col3 = st.columns([1, 0.09, 0.09])
                with fb_col1:
                    st.markdown("<span style='font-weight: 500;'>Is this helpful?</span>", unsafe_allow_html=True)
                with fb_col2:
                    thumbs_up = st.button("👍", key=f"thumbs_up_{idx}")
                with fb_col3:
                    thumbs_down = st.button("👎", key=f"thumbs_down_{idx}")
                if thumbs_up or thumbs_down:
                    st.markdown("<div style='color: white; margin-top: 4px;'>Thanks for the response!</div>", unsafe_allow_html=True)
           
        autoscroll_placeholder = st.empty()
        autoscroll_placeholder.markdown(" ")
                
                    
                
