# Create styles for ttk widgets
import re

def sanitizeInput(input_text):
    # 1. Strip away leading or trailing whitespaces
    sanitized_text = input_text.strip()
    
    # 2. Remove potentially harmful characters
    sanitized_text = re.sub(r'[^a-zA-Z0-9.,!?;: \-]', '', sanitized_text)

    return sanitized_text





def fetch_matches():
    return [{"team_names": "TeamA vs TeamB"}]



def close_match():
    print("Closing match")

def add_comment():
    print("Adding comment")

