import json
from datetime import datetime

from args import args


# load tasks
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as f:
            tasks = json.load(f)
            return tasks if isinstance(tasks, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# save and write task to JSON file
def save_file(task_list, filename="tasks.json"):
    try:
        with open(filename, "w") as f:
            json.dump(task_list, f, indent=4)
    except EOFError as e:
        print(e, "Could not save file")


# add new task
def add_task():
    try:
        tasks = load_tasks()

        task_id = max((task["id"] for task in tasks), default=0) + 1

        now = datetime.now().strftime("%m-%d-%Y %H:%M")
        tasks.append(
            {
                "id": task_id,
                "description": args.description,
                "status": args.status,
                "created_at": now,
                "updated_at": now,
            }
        )

        save_file(tasks)
        print(f"Task added successfully (ID: {task_id})")
    except Exception as e:
        print(f"Error adding task: {e}")

# list tasks
def list_tasks(command):
    try:
        tasks = load_tasks()
        if not tasks:
            print("No tasks found")
            return

        print(f"{command}\n" + "-" * 25)

        if command == "all":
            filtered_tasks = tasks
        elif command == "in-progress":
            filtered_tasks = [
                t for t in tasks if t["status"] in ["todo", "doing"]
            ]
        else:
            filtered_tasks = [t for t in tasks if t["status"] == command]

        for task in filtered_tasks:
            print(
                f"ID: {task['id']}, Task: {task['description']}, Status: {task['status']}, {task['updated_at']}"
            )

        if not filtered_tasks:
            print(f"No tasks found for {command}")

    except Exception as e:
        print(f"Error listing tasks: {e}")


# delete task
def delete_task(task_id):
    try:
        tasks = load_tasks()
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                save_file(tasks)
                print(
                    f"Task ID: {task_id}, '{deleted_task['description']}' successfully deleted"
                )
                return
        print(f"Task with ID {task_id} not found")

    except Exception as e:
        print(f"Error deleting task: {e}")


# mark task as done or in progress
def update_task(task_id, task_status):
    try:
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = task_status
                task["updated_at"] = datetime.now().strftime("%m-%d-%Y %H:%M")
                save_file(tasks)
                print(
                    f"Task ID: {task_id}, '{task['description']}' successfully updated to '{task_status}'"
                )
                return

        print(f"Task with ID {task_id} not found.")
    except Exception as e:
        print(f"Error updating task: {e}")


def main():
    commands = {
        "add": lambda: add_task()
        if args.description and args.status
        else None,
        "list": lambda: list_tasks(args.status),
        "delete": lambda: delete_task(args.id),
        "update": lambda: update_task(args.update_id, args.update_status),
    }
    if args.command in commands:
        result = commands[args.command]()


if __name__ == "__main__":
    main()
