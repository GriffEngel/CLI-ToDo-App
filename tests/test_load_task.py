import unittest
from unittest.mock import patch, mock_open, MagicMock
from datetime import datetime
import json

from main import load_tasks, add_task, save_file, args


# TODO: Write tests
class TestLoadTask(unittest.TestCase):
    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [
                {
                    "id": 1,
                    "description": "Do the dishes",
                    "status": "todo",
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]
        ),
    )
    def test_load_tasks(self, mock_open):
        filename = "tasks.json"
        # call function that is being tested
        actual_output = load_tasks(filename)
        # make sure it's being opened with correct arguments
        mock_open.assert_called_with(filename, "r")
        expected_output = [
            {
                "id": 1,
                "description": "Do the dishes",
                "status": "todo",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        ]

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
