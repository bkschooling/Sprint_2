import unittest
from contact_manager import add_contact, view_contacts, update_contact, delete_contact, contacts

class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Clear the contacts list before each test
        contacts.clear()

    def test_add_contact(self):
        result = add_contact("Alice", "123-456-7890")
        self.assertEqual(result, "Contact 'Alice' with phone '123-456-7890' added.")
        self.assertIn({"name": "Alice", "phone": "123-456-7890"}, contacts)

    def test_view_contacts_empty(self):
        result = view_contacts()
        self.assertEqual(result, "No contacts available.")

    def test_view_contacts_with_entries(self):
        add_contact("Alice", "123-456-7890")
        add_contact("Bob", "987-654-3210")
        result = view_contacts()
        self.assertIn("1. Alice - 123-456-7890", result)
        self.assertIn("2. Bob - 987-654-3210", result)

    def test_update_contact(self):
        add_contact("Alice", "123-456-7890")
        result = update_contact(0, "Alice Smith", "555-555-5555")
        self.assertEqual(result, "Contact 'Alice' updated to 'Alice Smith' with phone '555-555-5555'.")
        self.assertIn({"name": "Alice Smith", "phone": "555-555-5555"}, contacts)

    def test_update_contact_out_of_range(self):
        result = update_contact(0, "Alice Smith", "555-555-5555")
        self.assertEqual(result, "Error: Contact index out of range.")

    def test_delete_contact(self):
        add_contact("Alice", "123-456-7890")
        result = delete_contact(0)
        self.assertEqual(result, "Contact 'Alice' deleted.")
        self.assertNotIn({"name": "Alice", "phone": "123-456-7890"}, contacts)

    def test_delete_contact_out_of_range(self):
        result = delete_contact(0)
        self.assertEqual(result, "Error: Contact index out of range.")

if __name__ == '__main__':
    unittest.main()
