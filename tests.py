import unittest
from unittest.mock import patch, mock_open
from datetime import datetime
import json

from main import load_tasks

# TODO: Write tests
class TestMyFunctions(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            {
                "id": 1,
                "Description": "Do this dishes",
                "status": "todo",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        ),
    )
    def test_load_tasks(self, filename):
        expected_output = {
            "id": 1,
            "Description": "Do this dishes",
            "status": "todo",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        filename = "tasks.json"
        actual_output = load_tasks(filename)

        mock_file.assert_called_with(filename)

        self.assertEqual(expected_output, actual_output)
