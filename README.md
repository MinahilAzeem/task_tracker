# Task Tracker

A menu-based Python program for keeping track of everyday tasks. Tasks are saved in `tasks.json` and loaded when the program starts again.

## Features
- Add a task with Pending status.
- View numbered tasks and their status.
- Mark a task as Done.
- Delete a task by number.
- Save automatically after adding, completing or deleting.
- Handle blank titles, invalid choices, invalid task numbers and a missing save file.

## Run locally
Python 3 is required. No additional packages are needed.

Open a terminal in the project folder:

```bash
python mini_task_tracker.py
```

## Run in Google Colab
Open `Task_Tracker_Colab.ipynb` in Colab and run its cells in order. It writes the program into the current runtime, then runs it with `%run mini_task_tracker.py`.

To check persistence, add a task, choose 5 to exit, then run the program cell again in the same runtime. View the tasks to confirm they were reloaded.

Colab runtime files are temporary. Use the notebook's optional download cell to keep `tasks.json` before the runtime is reset. Keep your own task data private.

## Program structure
- `load_tasks()` reads JSON or returns an empty list if no file exists.
- `save_tasks()` writes the task list using `json.dump()`.
- `add_task()`, `view_tasks()`, `complete_task()` and `delete_task()` handle the menu actions.
- `choose_task()` validates a task number.
- `main()` loads saved tasks and repeats the menu until Exit.

A task looks like `{"title": "Read notes", "done": false}` in JSON. Python uses `False` and `True`; JSON uses `false` and `true`.

## Manual checks
1. Add `Read notes`, then View: it should be Pending.
2. Complete task 1, then View: it should be Done.
3. Exit and rerun in the same folder/runtime: the task should remain.
4. Try a blank title, menu choice 9, task number `abc`, 0 and 999.
5. Delete task 1, then View: it should be gone.
6. With no tasks, try Complete and Delete: the program should show a helpful message.

## Submission
Github: https://github.com/MinahilAzeem/task_tracker

Keep the Colab notebook as an optional supporting file. Do not upload `.venv`.
