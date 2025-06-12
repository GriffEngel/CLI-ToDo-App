import json
import argparse
from datetime import datetime
import os


# argparse setup
parser = argparse.ArgumentParser()

# subparsers
subparsers = parser.add_subparsers(dest="command")
add_parser = subparsers.add_parser("add", help="Add new task")
list_parser = subparsers.add_parser(
    "list", help="list tasks with the same status (todo, in-progress, done)"
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
    choices=["todo", "doing", "done"],
)

# list args
list_parser.add_argument(
    "status",
    help="Choose which status you would like to see all the tasks for",
    choices=["todo", "doing", "done"],
)

# delete args
delete_parser.add_argument(
    "id", type=int, help="Task ID you would like to delete"
)

# update args
update_parser.add_argument("update_id", help="Task ID you would like to update")
update_parser.add_argument(
    "update_status", help="What status you would like to change the task to"
)

# arguments
args = parser.parse_args()


# load tasks
def load_tasks(filename="tasks.json"):
    try:
        # reads file tasks.json
        with open(filename, "r") as f:
            # loads json data in file
            tasks = json.load(f)
            # returns data if tasks is a list, else returns a list
            return tasks if isinstance(tasks, list) else []
    # handles errors by returning a list
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# save and write task to JSON file
def save_file(task_list, filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(task_list, f, indent=4)


# add new task
def add_task():
    tasks = load_tasks()

    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": args.description,
        "status": args.status,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    tasks.append(task)

    save_file(tasks)


# list tasks
def list_tasks(command):
    tasks = load_tasks()
    print(f"{command}\n-------------------------")
    for task in tasks:
        if task["status"] == command:
            print(
                f"ID: {task['id']}, Task: {task['description']}, {task['created_at']}"
            )


# delete task
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
    save_file(tasks)


# TODO: debug function
# mark task as done or in progress
def update_task(task_id, task_status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = task_status
    print(tasks)


def main():
    if args.command == "add" and args.description and args.status:
        add_task()

    if args.command == "list":
        list_tasks(args.status)

    if args.command == "delete":
        delete_task(args.id)

    if args.command == "update":
        update_task(args.update_id, args.update_status)


if __name__ == "__main__":
    main()
