import unittest
from unittest.mock import patch
from models.match import Match, requestMatches, allMatches

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.data = {
            'match-id': 1,
            'visiting-team-name': 'TeamA',
            'visiting-team-quote': 1.5,
            'receiving-team-name': 'TeamB',
            'receiving-team-quote': 2,
            'match-date': '2023-08-25',
            'match-kickoff': '14:00:00',
            'match-end': '16:00:00',
            'is-closed': 0,
            'score': '2:2',
            'match-weather-forecast': 'Sunny',
            'match-commentaries': 'Good game!',
            'bets': []
        }
        self.match = Match(self.data)

    def test_is_future(self):
        self.assertFalse(self.match.is_future())

    def test_str(self):
        self.assertIn("OPEN", str(self.match))
        self.assertNotIn("IN THE FUTURE", str(self.match))
        self.assertNotIn("CLOSED", str(self.match))

    def test_is_live(self):  # being careful with this one 
        self.assertFalse(self.match.is_live())

    def test_is_open(self):
        self.assertTrue(self.match.is_open())


class TestUtilityFunctions(unittest.TestCase):

    @patch('models.match.getMatches')
    def test_requestMatches(self, mock_getMatches):
        mock_data = [
            {
                'match-id': 1,
                'visiting-team-name': 'TeamA',
                'visiting-team-quote': 1.5,
                'receiving-team-name': 'TeamB',
                'receiving-team-quote': 2,
                'match-date': '2023-08-25',
                'match-kickoff': '14:00:00',
                'match-end': '16:00:00',
                'is-closed': 0,
                'score': '2:2',
                'match-weather-forecast': 'Sunny',
                'match-commentaries': 'Good game!',
                'bets': []
            },
            {
                'match-id': 2,
                'visiting-team-name': 'TeamA',
                'visiting-team-quote': 3,
                'receiving-team-name': 'TeamB',
                'receiving-team-quote': 2,
                'match-date': '2023-08-25',
                'match-kickoff': '20:00:00',
                'match-end': '21:00:00',
                'is-closed': 1,
                'score': '2:2',
                'match-weather-forecast': 'Sunny',
                'match-commentaries': 'Good game!',
                'bets': []
            }
        ]
        mock_getMatches.return_value = mock_data

        requestMatches()
        self.assertEqual(len(allMatches()), 2)


if __name__ == '__main__':
    unittest.main()
