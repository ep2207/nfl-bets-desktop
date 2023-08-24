import datetime


class Bet:
    def __init__(self, data):
        self.bet_id = data['bet_id']
        self.team_bet_on = data['team_bet_on']
        self.bet_amount = data['bet_amount']
        self.bet_result = data['bet_result']

    def __str__(self):
        return f"Bet ID {self.bet_id} on {self.team_bet_on}: Amount {self.bet_amount} $, Result {self.bet_result} $"

    def calculate_gain(self, visiting_team, receiving_team,visiting_team_quote, receiving_team_quote, score):
        # Split score and convert to integers
        visiting_score, receiving_score = map(int, score.split(":"))

        # Determine the actual winning team based on the scores
        if visiting_score > receiving_score:
            actual_winning_team = visiting_team
        elif receiving_score > visiting_score:
            # Assuming you have both team's names, we find the one that's not the visiting team
            actual_winning_team = receiving_team if self.team_bet_on != visiting_team else visiting_team
        else:  # It's a tie
            return 0  

        # If the user didn't bet on the actual winning team, then there's no gain
        if self.team_bet_on != actual_winning_team:
            return 0   

        # Calculate the odds and return the potential gain
        if self.team_bet_on == visiting_team:
            odds = receiving_team_quote / visiting_team_quote
        else:
            odds = visiting_team_quote / receiving_team_quote

        return self.bet_amount * odds

def separate_bets_by_team(match):
    visiting_team_bets = []
    receiving_team_bets = []


    for bet in match.bets:
        if bet.team_bet_on == match.visiting_team_name:
            visiting_team_bets.append(bet)
        elif bet.team_bet_on == match.receiving_team_name:
            receiving_team_bets.append(bet)
    
    return visiting_team_bets, receiving_team_bets


def total_bet_amount(bets):
    return sum(bet.bet_amount for bet in bets)

     


