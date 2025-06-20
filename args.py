import argparse

# argparse setup
parser = argparse.ArgumentParser()

# subparsers
subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add", help="Add new task")
list_parser = subparsers.add_parser(
    "list",
    help="list tasks with the same status (todo, in-progress, done)",
)
delete_parser = subparsers.add_parser(
    "delete", help="remove task from task list"
)
update_parser = subparsers.add_parser("update", help="Update a task")

# add args
add_parser.add_argument(
    "description",
    help="Enter the task you wish to track in quotes",
    type=str,
)
add_parser.add_argument(
    "status",
    help="Are you not started, in-progress, or done with the task?",
    default="todo",
    nargs="?",
    choices=("todo", "doing", "done"),
)

# list args
list_parser.add_argument(
    "status",
    help="Choose which status you would like to see all the tasks for",
    choices=("todo", "doing", "done", "all", "in-progress"),
)

# delete args
delete_parser.add_argument(
    "id", type=int, help="Task ID you would like to delete"
)

# update args
update_parser.add_argument(
    "update_id", type=int, help="Task ID you would like to update"
)
update_parser.add_argument(
    "update_status",
    help="What status you would like to change the task to",
)

# arguments
args = parser.parse_args()
