import unittest
from models.bet import Bet, separate_bets_by_team, total_bet_amount

class TestBet(unittest.TestCase):

    def setUp(self):
        self.data = {
            'bet_id': 1,
            'team_bet_on': 'TeamA',
            'bet_amount': 100,
            'bet_result': 200
        }
        self.bet = Bet(self.data)

    def test_str(self):
        self.assertEqual(str(self.bet), "Bet ID 1 on TeamA: Amount 100 $, Result 200 $")

    def test_calculate_gain(self):
        # Test when visiting team wins
        gain = self.bet.calculate_gain('TeamA', 'TeamB', 1, 2, '3:2')
        self.assertEqual(gain, 100 * (2/1))

        # Test when receiving team wins and the bet was on the visiting team
        gain = self.bet.calculate_gain('TeamA', 'TeamB', 1, 2, '2:30')
        self.assertEqual(gain, 0)

        # Test when there's a tie
        gain = self.bet.calculate_gain('TeamA', 'TeamB', 1, 2, '2:2')
        self.assertEqual(gain, 0)

class TestUtilityFunctions(unittest.TestCase):

    def setUp(self):
        data1 = {
            'bet_id': 1,
            'team_bet_on': 'TeamA',
            'bet_amount': 100,
            'bet_result': 100
        }
        data2 = {
            'bet_id': 2,
            'team_bet_on': 'TeamB',
            'bet_amount': 150,
            'bet_result': 0
        }
        self.bet1 = Bet(data1)
        self.bet2 = Bet(data2)
        self.match = type('', (), {})() # Create a mock match object
        self.match.bets = [self.bet1, self.bet2]
        self.match.visiting_team_name = 'TeamA'
        self.match.receiving_team_name = 'TeamB'

    def test_separate_bets_by_team(self):
        visiting_bets, receiving_bets = separate_bets_by_team(self.match)
        self.assertEqual(len(visiting_bets), 1)
        self.assertEqual(len(receiving_bets), 1)

    def test_total_bet_amount(self):
        bets = [self.bet1, self.bet2]
        self.assertEqual(total_bet_amount(bets), 250)

if __name__ == '__main__':
    unittest.main()
