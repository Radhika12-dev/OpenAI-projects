def load_openai_key(filepath='key.txt'):
    with open(filepath, 'r') as f:
        key = f.read().strip()
        assert key.startswith('sk-'), "Invalid OpenAI API key format."
    return key
