import unittest
from unittest.mock import patch, Mock
from queries.post_queries import getMatches, postCommentary, closeMatch

class TestApiFunctions(unittest.TestCase):

    def setUp(self):
        # This is a mock response object to simulate the response returned from requests.post
        self.mock_response = Mock()
        self.mock_response.status_code = 200
        self.mock_response.json.return_value = {"key": "value"}

    @patch('queries.post_queries.requests.post') # Mock requests.post method
    def test_getMatches(self, mock_post):
        # Setup mock response
        mock_post.return_value = self.mock_response

        response = getMatches()
        self.assertEqual(response, {"key": "value"})

    @patch('queries.post_queries.requests.post') # Mock requests.post method
    def test_postCommentary(self, mock_post):
        # Setup mock response
        mock_post.return_value = self.mock_response

        response = postCommentary(1, "<script>bad()</script>")
        self.assertEqual(response, {"key": "value"})

    @patch('queries.post_queries.requests.post') # Mock requests.post method
    def test_closeMatch(self, mock_post):
        # Setup mock response
        mock_post.return_value = self.mock_response

        response = closeMatch({"key": "value"})
        self.assertEqual(response, {"key": "value"})

if __name__ == "__main__":
    unittest.main()
