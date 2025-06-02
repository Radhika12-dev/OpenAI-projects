import os
def load_key():
    key_path = os.path.join(os.path.dirname(__file__), 'diet_planner_key.txt')
    with open(key_path, 'r') as f:
        api_key = f.read().strip('\n')
        assert api_key.startswith('sk-') , 'Error loading API key'
    
    return api_key