tasks = []

def add_task(task, priority="Medium", due_date=None):
    """Adds a new task to the list with a priority and optional due date."""
    tasks.append({"task": task, "priority": priority, "due_date": due_date})
    return f"Task '{task}' added with priority '{priority}' and due date '{due_date}'."

def view_tasks():
    """Returns all tasks in the list."""
    if not tasks:
        return "No tasks available."
    result = []
    for i, task in enumerate(tasks):
        due_date = task["due_date"] if task["due_date"] else "None"
        result.append(f"{i + 1}. {task['task']} (Priority: {task['priority']}, Due: {due_date})")
    return "\n".join(result)

def update_task(index, new_task=None, new_priority=None, new_due_date=None):
    """Updates the task at the given index."""
    try:
        if new_task:
            tasks[index]["task"] = new_task
        if new_priority:
            tasks[index]["priority"] = new_priority
        if new_due_date:
            tasks[index]["due_date"] = new_due_date
        return f"Task {index + 1} updated successfully."
    except IndexError:
        return "Error: Task index out of range."

def delete_task(index):
    """Deletes the task at the given index."""
    try:
        task = tasks.pop(index)
        return f"Task '{task['task']}' deleted."
    except IndexError:
        return "Error: Task index out of range."

def search_tasks(keyword):
    """Searches for tasks containing the given keyword."""
    matches = [f"{i + 1}. {task['task']} (Priority: {task['priority']})"
               for i, task in enumerate(tasks) if keyword.lower() in task["task"].lower()]
    return "\n".join(matches) if matches else "No matching tasks found."
