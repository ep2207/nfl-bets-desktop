import unittest
from unittest.mock import Mock, patch
from main import get_selected_match 

class TestMainFunctions(unittest.TestCase):
    @patch('main.match_listbox.curselection', return_value=(0,))
    def test_get_selected_match_with_selection(self, mock_curselection):
        mock_match = Mock()
        global matches
        matches = [mock_match]
        
        result = get_selected_match()

        self.assertEqual(result, mock_match)

    @patch('main.match_listbox.curselection', return_value=())
    def test_get_selected_match_without_selection(self, mock_curselection):
        result = get_selected_match()
        self.assertIsNone(result)

class TestCloseMatchFunction(unittest.TestCase):
    @patch('main.messagebox.askyesno', return_value=True)
    @patch('main.get_selected_match')
    @patch('main.visiting_team_score_entry.get', return_value='5')
    @patch('main.receiving_team_score_entry.get', return_value='3')
    def test_close_match(self, mock_v_score, mock_r_score, mock_get_selected_match, mock_askyesno):
        mock_match = Mock()
        mock_match.score = None
        mock_get_selected_match.return_value = mock_match
        
        close_match()
        
        self.assertEqual(mock_match.score, '5:3')

if __name__ == '__main__':
    unittest.main()