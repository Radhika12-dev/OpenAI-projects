import streamlit as st
import openai
from utils import load_openai_key
from constants import EMOTIONS



def get_classify_sentiment(prompt, emotions):
    system_prompt = f"""You are an emotionally intelligent assistant.
    Classify the sentiment of the user's text with only one of the following emotions: {emotions}.
    After classifying the sentiment, return the emotion and add explaination or facts or information related to the text entered by user."""

    response = openai.chat.completions.create(
        model ="gpt-4.1-nano",
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}

        ],
        max_tokens=100,
        temperature=0.0,

    )
    r = response.choices[0].message.content
    if r == '':
        r = 'neutral'
    return r

if __name__ == "__main__":
    openai.api_key = load_openai_key()
    st.set_page_config(page_title="Zero-Shot Sentiment Analysis", page_icon=":robot_face:")
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.title("Zero-Shot Sentiment Analysis")
        st.subheader("Classify text sentiment using OpenAI's GPT model.")
    with col2:
        st.image('ai.jpeg', width=70)

    st.markdown("---")
    with st.form(key='sentiment_form'):
        default_emotions = EMOTIONS
        emotions = st.text_input('Emotions (comma-separated)', value=default_emotions)
        text = st.text_area(label='Text to classify', height=120)
        submit_button = st.form_submit_button(label='Classify Sentiment')

        if submit_button:
            if not text.strip():
                st.warning("Please enter some text to classify.")
            else:
                emotion = get_classify_sentiment(text, emotions)
                st.success(f"The classified sentiment is: **{emotion}**")

    st.sidebar.header("Instructions")
    st.sidebar.write(
        "1. Enter or edit the list of emotions (comma-separated).\n"
        "2. Type or paste the text you want to classify.\n"
        "3. Click 'Classify Sentiment' to see the result."
    )
        




