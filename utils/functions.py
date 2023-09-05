import datetime as dt
import json 


def sanitizeInput(input_text):
    # Characters to remove
    # You can expand this list based on your requirements
    dangerous_chars = ['<', '>', ';', '&', '|', '$', '`', '!', '*']

    # Remove dangerous characters
    for char in dangerous_chars:
        input_text = input_text.replace(char, '')

    # Strip away leading or trailing whitespaces
    return input_text.strip()



def getClosureData(selected_match):
    # Check if the match is live 
    if  selected_match.is_open():
        # Set the match end-time to the current time
        current_time = dt.datetime.now().strftime('%I:%M:%S %p')
        selected_match.match_end = current_time  # Update the match end time

        # Calculate bet results and populate the bets list


        bets_list = []
        for bet in selected_match.bets:
            bet.bet_result = bet.calculate_gain(selected_match.visiting_team_name,selected_match.receiving_team_name,
                                                selected_match.visiting_team_quote, selected_match.receiving_team_quote, 
                                                selected_match.score) 
            bets_list.append({
                "bet-id": bet.bet_id,
                "bet-result": bet.bet_result
            })

        # Construct the JSON
        if bets_list:
            match_data = {
                "match-id": str(selected_match.match_id),
                "match-end": current_time,
                "score":str(selected_match.score),
                "bets": bets_list
                }            
            json_data = json.dumps(match_data) 
            return json_data
        
        else: 
            match_data = {
                "match-id": str(selected_match.match_id),
                "match-end": current_time,
                "score":str(selected_match.score)
                }
            json_data = json.dumps(match_data)
            return json_data


