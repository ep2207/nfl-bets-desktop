import datetime


class Bet:
    def __init__(self, data):
        self.bet_id = data['bet_id']
        self.team_bet_on = data['team_bet_on']
        self.bet_amount = data['bet_amount']
        self.bet_result = data['bet_result']

    def __str__(self):
        return f"Bet ID {self.bet_id} on {self.team_bet_on}: Amount {self.bet_amount} $, Result {self.bet_result} $"

    def calculate_gain(self, visiting_team_quote, receiving_team_quote):
        if self.team_bet_on == "visiting_team":
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

     


