import unittest
from unittest.mock import patch
from io import StringIO
import flask.asin as fa

class TestMain(unittest.TestCase):
    def setUp(self):
        self.asin = 'B01B1VC13K'
        self.email = 'test@example.com'
        self.notification_type = 0
        self.current_price = 12.99
        self.product_name = 'Example Product'

    @patch('fa.requests.request')
    def test_api_call(self, mock_request):
        mock_request.return_value.content = '[{"current_price": "12.99"}]'.encode('utf-8')
        expected_price = self.current_price
        actual_price = fa.api_call()
        self.assertEqual(expected_price, actual_price)

    @patch('fa.cursor.execute')
    @patch('fa.mydb.commit')
    def test_update_db(self, mock_commit, mock_execute):
        expected_query = "UPDATE email_tracker SET curr_price = %s WHERE ASIN = %s"
        expected_params = (self.current_price, self.asin)
        fa.update_db(self.current_price)
        mock_execute.assert_called_once_with(expected_query, expected_params)
        mock_commit.assert_called_once()

    @patch('fa.cursor.fetchone')
    def test_get_from_db(self, mock_fetchone):
        expected_result = (self.current_price, self.product_name)
        mock_fetchone.return_value = (self.current_price, self.product_name)
        actual_result = fa.get_from_db()
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()