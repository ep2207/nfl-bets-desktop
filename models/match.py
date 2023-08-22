from get_queries import getMatches


class Match:
    def __init__(self, match_id, visiting_team_name, visiting_team_quote, receiving_team_name,
                 receiving_team_quote, match_date, match_kickoff, match_end, score, match_weather_forecast, bets, match_commentaries):
        self.match_id = match_id
        self.visiting_team_name = visiting_team_name
        self.visiting_team_quote = visiting_team_quote
        self.receiving_team_name = receiving_team_name
        self.receiving_team_quote = receiving_team_quote
        self.match_date = match_date
        self.match_kickoff = match_kickoff
        self.match_end = match_end
        self.score = score
        self.match_weather_forecast = match_weather_forecast
        self.bets = bets
        self.match_commentaries = match_commentaries

    def __str__(self):
        return f"Match {self.match_id}: {self.visiting_team_name} vs {self.receiving_team_name} on {self.match_date}"

listOfMatches =[]

def requestMatches():
    global listOfMatches
    data = getMatches()
    # Clear the current data
    listOfMatches.clear()
    # Extend the global list with new matches
    listOfMatches.extend([Match(**match) for match in data])

def allMatches():
    global listOfMatches
    # Always refresh the data whenever you call allMatches
    requestMatches()
    return listOfMatches

# To get and refresh the data, simply call allMatches
matches = allMatches()