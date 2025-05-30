# Helping Agent (ChatGPT-Clone)

A Streamlit-based conversational AI assistant powered by OpenAI's GPT models.  
This project features persistent question history, feedback buttons, and a clean, user-friendly interface.

## Features

- **Chat with GPT:** Ask questions and get intelligent responses.
- **Persistent History:** All your questions are saved and shown in the sidebar, even after restarting the app.
- **History Expiry:** Questions older than 7 days are automatically deleted.
- **Clickable History:** Click any previous question to re-ask or edit it.
- **Feedback:** Give a thumbs up or down for each bot response.
- **Modern UI:** Responsive layout, chat bubbles, and clear separation of history and chat.

## Setup

1. **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd chatgpt-clone
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # Or
    source venv/bin/activate  # On Mac/Linux
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set your OpenAI API key:**
    - Add your API key to a file named `key.txt` or use Streamlit secrets (`.streamlit/secrets.toml`).

5. **Run the app:**
    ```bash
    streamlit run chatgpt_clone.py
    ```

## File Structure

- `chatgpt_clone.py` — Main Streamlit app.
- `history.json` — Stores user question history (auto-managed).
- `.gitignore` — Ignores secrets, history, and environment files.
- `requirements.txt` — Python dependencies.
- `README.md` — This file.

## Notes

- **Security:** Never commit your OpenAI API key to version control.
- **Customization:** You can adjust the UI, feedback logic, and history expiry in the code.
- **Feedback:** Thumbs up/down feedback is for UI only; you can extend it to log or analyze responses.

## License

MIT License

---

**Enjoy your AI-powered Helping Agent!**