import unittest
from todo_list import add_task, view_tasks, update_task, delete_task, search_tasks, tasks

class TestTodoList(unittest.TestCase):

    def setUp(self):
        # Clear the tasks list before each test
        tasks.clear()

    def test_add_task(self):
        result = add_task("Read a book", "High", "2024-12-01")
        self.assertEqual(result, "Task 'Read a book' added with priority 'High' and due date '2024-12-01'.")
        self.assertIn({"task": "Read a book", "priority": "High", "due_date": "2024-12-01"}, tasks)

    def test_view_tasks_empty(self):
        result = view_tasks()
        self.assertEqual(result, "No tasks available.")

    def test_view_tasks_with_entries(self):
        add_task("Read a book", "Medium", None)
        add_task("Write a report", "High", "2024-12-10")
        result = view_tasks()
        self.assertIn("1. Read a book (Priority: Medium, Due: None)", result)
        self.assertIn("2. Write a report (Priority: High, Due: 2024-12-10)", result)

    def test_update_task(self):
        add_task("Read a book", "Medium", None)
        result = update_task(0, new_task="Read two books", new_priority="High", new_due_date="2024-11-30")
        self.assertEqual(result, "Task 1 updated successfully.")
        self.assertIn({"task": "Read two books", "priority": "High", "due_date": "2024-11-30"}, tasks)

    def test_update_task_out_of_range(self):
        result = update_task(0, new_task="Invalid task")
        self.assertEqual(result, "Error: Task index out of range.")

    def test_delete_task(self):
        add_task("Read a book", "Medium", None)
        result = delete_task(0)
        self.assertEqual(result, "Task 'Read a book' deleted.")
        self.assertNotIn({"task": "Read a book", "priority": "Medium", "due_date": None}, tasks)

    def test_delete_task_out_of_range(self):
        result = delete_task(0)
        self.assertEqual(result, "Error: Task index out of range.")

    def test_search_tasks(self):
        add_task("Read a book", "Medium", None)
        add_task("Write a report", "High", None)
        result = search_tasks("read")
        self.assertIn("1. Read a book (Priority: Medium)", result)
        self.assertNotIn("Write a report", result)

    def test_search_tasks_no_match(self):
        result = search_tasks("not in list")
        self.assertEqual(result, "No matching tasks found.")

if __name__ == '__main__':
    unittest.main()
