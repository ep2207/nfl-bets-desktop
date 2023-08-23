import datetime
from queries.post_queries import getMatches
from models.bet import Bet
from datetime import datetime

class Match:
    def __init__(self, data):
        self.match_id = data['match-id']
        self.visiting_team_name = data['visiting-team-name']
        self.visiting_team_quote = data['visiting-team-quote']
        self.receiving_team_name = data['receiving-team-name']
        self.receiving_team_quote = data['receiving-team-quote']
        self.match_date = data['match-date']
        self.match_kickoff = data['match-kickoff']
        self.match_end = data['match-end']
        self.score = data['score']
        self.match_weather_forecast = data['match-weather-forecast']
        self.match_commentaries = data['match-commentaries']
        
        #handle bets in case of empty data 
        bets_data = data.get('bets')
        if bets_data is None:
            self.bets = []
        else:
            self.bets = [Bet(bet_data) for bet_data in bets_data]


    def __str__(self):
        return f"{self.match_date} Match {self.match_id}: {self.visiting_team_name} vs {self.receiving_team_name}"

    def is_live(self):
        # Assuming match_date, match_kickoff, and match_end are in the format 'YYYY-MM-DD HH:MM'
        match_date = datetime.strptime(self.match_date, '%Y-%m-%d').date()
        kickoff_time = datetime.strptime(f"{self.match_date} {self.match_kickoff}", '%Y-%m-%d %H:%M')
        end_time = datetime.strptime(f"{self.match_date} {self.match_end}", '%Y-%m-%d %H:%M')
        current_time = datetime.now()

        return kickoff_time <= current_time <= end_time and match_date == current_time.date()

listOfMatches = []


def requestMatches():
    global listOfMatches
    data = getMatches()
    # Clear the current data
    listOfMatches.clear()
    # Extend the global list with new matches
    listOfMatches.extend([Match(match) for match in data])

def allMatches():
    global listOfMatches
    # Always refresh the data whenever you call allMatches
    requestMatches()
    return listOfMatches

# To get and refresh the data, simply call allMatches
matches = allMatches()

