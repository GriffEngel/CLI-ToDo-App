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


# applied bottom to top?
@patch("main.save_file")
@patch("main.load_tasks")
@patch("main.args")
@patch("main.datetime")
class TestAddTask(unittest.TestCase):
    def test_add_task_success(
        self, mock_datetime, mock_args, mock_load_tasks, mock_save_file
    ):
        # mock data
        mock_load_tasks.return_value = [
            {"id": 1, "description": "Test Task", "status": "todo"}
        ]
        mock_args.description = "Do the dishes"
        mock_args.status = "todo"

        # mock datetime to return consistent values
        mock_now = MagicMock()
        # set constant time
        mock_now.strftime.return_value = "2024-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now

        add_task()

        # verify load_tasks called
        mock_load_tasks.assert_called_once()

        # verify save_file
        mock_save_file.assert_called_once()

        saved_tasks = mock_save_file.call_args[0][0]

        # verify new task added correctly
        self.assertEqual(len(saved_tasks), 2)
        new_task = saved_tasks[1]
        self.assertEqual(new_task["id"], 2)
        self.assertEqual(new_task["description"], "Do the dishes")
        self.assertEqual(new_task["status"], "todo")
        self.assertEqual(new_task["created_at"], "2024-01-01 12:00:00")
        self.assertEqual(new_task["updated_at"], "2024-01-01 12:00:00")

    def test_add_task_duplicate_id(
        self, mock_datetime, mock_args, mock_load_tasks, mock_save_file
    ):
        mock_load_tasks.return_value = [
            {"id": 1, "description": "Test Task", "status": "todo"},
            {"id": 2, "description": "Test Task", "status": "todo"},
            {"id": 3, "description": "Test Task", "status": "todo"},
            {"id": 5, "description": "Test Task", "status": "todo"},
        ]

        mock_args.description = "Do the dishes"
        mock_args.status = "todo"

        # mock datetime to return consistent values
        mock_now = MagicMock()
        # set constant time
        mock_now.strftime.return_value = "2024-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now

        add_task()
        mock_save_file.assert_called_once()

        saved_tasks = mock_save_file.call_args[0][0]

        new_task = saved_tasks[4]
        self.assertEqual(new_task["id"], 6)

    def test_add_task_empty_list(
        self, mock_datetime, mock_args, mock_load_tasks, mock_save_file
    ):
        mock_load_tasks.return_value = []

        mock_args.description = "Do the dishes"
        mock_args.status = "todo"

        mock_now = MagicMock()
        mock_now.strftime.return_value = "2024-01-01 12:00:00"
        mock_datetime.now.return_value = mock_now

        add_task()

        mock_save_file.assert_called_once()

        saved_tasks = mock_save_file.call_args[0][0]

        self.assertEqual(len(saved_tasks), 1)
        self.assertEqual(saved_tasks[0]["id"], 1)


if __name__ == "__main__":
    unittest.main()
