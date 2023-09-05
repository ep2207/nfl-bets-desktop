import unittest
import sys
sys.path.append('../utils')
from unittest.mock import Mock
from functions import sanitizeInput, getClosureData  
import datetime as dt
import json


class TestFunctions(unittest.TestCase):
    
    def test_sanitizeInput(self):
    
        # Test for harmful characters removal
        self.assertEqual(sanitizeInput("<script>alert('hacked')</script>"), "")
        
        # Test for leading/trailing whitespace removal
        self.assertEqual(sanitizeInput("  hello  "), "hello")
        
        # Test for valid characters
        self.assertEqual(sanitizeInput("hello, world!"), "hello, world!")

    def test_getClosureData(self):
        # Mock a bet object
        mock_bet = Mock()
        mock_bet.bet_id = 1
        mock_bet.calculate_gain.return_value = 100
        
        # Mock a selected_match object
        mock_selected_match = Mock()
        mock_selected_match.is_open.return_value = True
        mock_selected_match.match_id = 1
        mock_selected_match.visiting_team_name = "TeamA"
        mock_selected_match.receiving_team_name = "TeamB"
        mock_selected_match.visiting_team_quote = 1.5
        mock_selected_match.receiving_team_quote = 2.5
        mock_selected_match.score = "1-1"
        mock_selected_match.bets = [mock_bet]
        
        # Call the function
        result = getClosureData(mock_selected_match)
        
        # Create the expected JSON result
        current_time = dt.datetime.now().strftime('%I:%M:%S %p')
        expected_result = {
            "match-id": "1",
            "match-end": current_time,
            "score": "1-1",
            "bets": [
                {
                    "bet-id": 1,
                    "bet-result": 100
                }
            ]
        }
        expected_json = json.dumps(expected_result)
        
        # Check if the result matches the expected JSON
        self.assertEqual(result, expected_json)

if __name__ == "__main__":
    unittest.main()
