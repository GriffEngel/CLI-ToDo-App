# [CLI ToDo -- A command line interface todo list](https://github.com/GriffEngel/CLI-ToDo-App)

## Adding a Task
### ``clitodo add <"description"> <status>``
  ``clitodo add "Do the dishes" todo``
  - Adds "Do this dishes" to your task list
  - ``add`` is the command, signifies this is a new task
  - ``"Do the dishes"`` is the description, put the description in quotation marks
  - ``<status>`` is optional, defaults to ``todo``

## Updating a task
### ``clitodo update <task_id> <status>``
``clitodo update 1 done``
- Updates the task with task id ``1`` to done
  - Can only update status at this time

## Listing Tasks
### ``clitodo list <status>``
``clitodo list all``
- Lists all tasks you have currently
- Can list tasks by status (``todo, doing, done``), ``in-progress`` to show all tasks not marked done, and ``all`` to show all tasks

## Deleting tasks
### ``clitodo delete <task_id>``
``clitodo delete 1``
- Deletes the task with task id ``1``

