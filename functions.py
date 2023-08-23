# Create styles for ttk widgets
import datetime
import json
import re

def sanitizeInput(input_text):
    # 1. Strip away leading or trailing whitespaces
    sanitized_text = input_text.strip()
    
    # 2. Remove potentially harmful characters
    sanitized_text = re.sub(r'[^a-zA-Z0-9.,!?;: \-]', '', sanitized_text)

    return sanitized_text


def getClosureData(selected_match):

    # Check if the match is live 
    if selected_match.is_live():
        # Set the match end-time to the current time
        current_time = datetime.now().strftime('%I:%M %p')  # Get the current time in 12-hour format with AM/PM
        selected_match.match_end = current_time  # Update the match end time

        # Calculate bet results and populate the bets list
        bets_list = []
        for bet in selected_match.bets:
            bet_result = bet.calculate_gain(selected_match.visiting_team_quote, selected_match.receiving_team_quote) 
            bets_list.append({
                "bet-id": bet.bet_id,
                "bet-result": bet_result
            })

        # Construct the JSON
        match_data = {
            "match-id": str(selected_match.match_id),
            "match-end": current_time,
            "bets": bets_list
        }

        json_data = json.dumps(match_data)
        return json_data

