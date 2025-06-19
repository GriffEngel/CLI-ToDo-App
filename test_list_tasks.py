import unittest
from unittest.mock import patch, mock_open, MagicMock
import json

from main import load_tasks, list_tasks, save_file, args


# applied bottom to top?
@patch("builtins.print")
@patch("main.load_tasks")
@patch("main.args")
class TestListTasks(unittest.TestCase):
    def test_list_tasks_all(self, mock_args, mock_load_tasks, mock_print):
        mock_load_tasks.return_value = [
            {
                "id": 1,
                "description": "do the dishes",
                "status": "todo",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
            {
                "id": 2,
                "description": "do the dishes",
                "status": "doing",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
            {
                "id": 3,
                "description": "do the dishes",
                "status": "done",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
        ]
        mock_args.command = "all"

        list_tasks(mock_args.command)

        mock_load_tasks.assert_called_once()
        expected = [
            unittest.mock.call("all\n-------------------------"),
            unittest.mock.call(
                "ID: 1, do the dishes, Status: todo, 2024-01-01 12:00:00"
            ),
            unittest.mock.call(
                "ID: 2, do the dishes, Status: doing, 2024-01-01 12:00:00"
            ),
            unittest.mock.call(
                "ID: 3, do the dishes, Status: done, 2024-01-01 12:00:00"
            ),
        ]

        mock_print.assert_has_calls(expected)

    def test_list_tasks_todo(self, mock_args, mock_load_tasks, mock_print):
        mock_load_tasks.return_value = [
            {
                "id": 1,
                "description": "do the dishes",
                "status": "todo",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
            {
                "id": 2,
                "description": "do the dishes",
                "status": "doing",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
            {
                "id": 3,
                "description": "do the dishes",
                "status": "done",
                "created_at": "2024-01-01 12:00:00",
                "updated_at": "2024-01-01 12:00:00",
            },
        ]

        mock_args.command = "todo"
        list_tasks(mock_args.command)

        mock_load_tasks.assert_called_once()
        expected = [
            unittest.mock.call(
                "ID: 1, Task: do the dishes, 2024-01-01 12:00:00"
            ),
        ]

        mock_print.assert_has_calls(expected)


if __name__ == "__main__":
    unittest.main()
