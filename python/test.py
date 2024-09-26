import unittest
from unittest.mock import patch
from client import grpc_stat, grpc_read, rest_stat, rest_read

class TestFileClient(unittest.TestCase):
    @patch('client.grpc_stat')
    def test_grpc_stat(self, mock_grpc_stat):
        mock_grpc_stat.return_value = {"name": "example.txt"}
        result = grpc_stat("localhost:50051", "some-uuid")
        self.assertEqual(result, {"name": "example.txt"})

    @patch('client.rest_stat')
    def test_rest_stat(self, mock_rest_stat):
        mock_rest_stat.return_value = {"name": "example.txt"}
        result = rest_stat("http://localhost/", "some-uuid")
        self.assertEqual(result, {"name": "example.txt"})

if __name__ == "__main__":
    unittest.main()