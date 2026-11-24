"""A small task tracker that remembers tasks between runs."""

import json

TASK_FILE = "tasks.json"
tasks = []


def load_tasks():
    """Read saved tasks, or start fresh on the first run."""
    try:
        with open(TASK_FILE, "r", encoding="utf-8") as saved_file:
            saved_tasks = json.load(saved_file)
        if not isinstance(saved_tasks, list) or any(
            not isinstance(task, dict)
            or not isinstance(task.get("title"), str)
            or not isinstance(task.get("done"), bool)
            for task in saved_tasks
        ):
            raise ValueError("Unexpected task format")
        return saved_tasks
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, ValueError):
        print("The saved task file could not be read. Check tasks.json before editing tasks.")
        raise SystemExit(1)


def save_tasks():
    """Save after a change so the next run can reload our list."""
    with open(TASK_FILE, "w", encoding="utf-8") as saved_file:
        json.dump(tasks, saved_file, indent=4, ensure_ascii=False)


def add_task():
    title = input("Task title: ").strip()
    if not title:
        print("Please enter a task title.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added.")


def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for number, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{number}. {task['title']} [{status}]")


def choose_task():
    """Convert the displayed task number into a list position."""
    view_tasks()
    if not tasks:
        return None
    try:
        number = int(input("Task number: "))
    except ValueError:
        print("Please enter a whole number.")
        return None
    if number < 1 or number > len(tasks):
        print("That task number is not in the list.")
        return None
    return number - 1


def complete_task():
    position = choose_task()
    if position is not None:
        tasks[position]["done"] = True
        save_tasks()
        print("Task completed.")


def delete_task():
    position = choose_task()
    if position is not None:
        removed = tasks.pop(position)
        save_tasks()
        print(f"Deleted: {removed['title']}")


def main():
    global tasks
    tasks = load_tasks()
    while True:
        print("\n--- TASK TRACKER ---")
        print("1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Your changes have been saved.")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
