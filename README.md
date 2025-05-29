# OpenAI-projects# Zero-Shot Sentiment Analysis App

This is a Streamlit web app that classifies the sentiment of user-provided text using OpenAI's GPT model in a zero-shot setting. You can specify your own list of emotions for classification.

## Features

- Zero-shot sentiment classification using OpenAI GPT
- Customizable list of emotions
- Simple and interactive Streamlit UI

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Radhika12-dev/OpenAI-projects.git
    cd your-repo/zero-shot-sentiment-analysis-app
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Add your OpenAI API key:**
    - Create a file named `key.txt` in the project directory.
    - Paste your OpenAI API key inside `key.txt` (the file is ignored by git).

4. **Run the app:**
    ```sh
    streamlit run zero-shot-sentiment-analysis.py
    ```

## Usage

- Enter or edit the list of emotions (comma-separated).
- Type or paste the text you want to classify.
- Click **Classify Sentiment** to see the result.

## Security

- **Never share your `key.txt` or API key publicly.**
- The `.gitignore` file ensures `key.txt` is not uploaded to GitHub.

## License

MIT License

---

**Made with ❤️ using Streamlit and OpenAI**