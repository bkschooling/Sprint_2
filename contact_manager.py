contacts = []

def add_contact(name, phone):
    """Adds a new contact to the list."""
    contacts.append({"name": name, "phone": phone})
    return f"Contact '{name}' with phone '{phone}' added."

def view_contacts():
    """Returns all contacts in the list."""
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{i + 1}. {contact['name']} - {contact['phone']}" for i, contact in enumerate(contacts))

def update_contact(index, new_name, new_phone):
    """Updates the contact at the given index."""
    try:
        old_contact = contacts[index]
        contacts[index] = {"name": new_name, "phone": new_phone}
        return f"Contact '{old_contact['name']}' updated to '{new_name}' with phone '{new_phone}'."
    except IndexError:
        return "Error: Contact index out of range."

def delete_contact(index):
    """Deletes the contact at the given index."""
    try:
        contact = contacts.pop(index)
        return f"Contact '{contact['name']}' deleted."
    except IndexError:
        return "Error: Contact index out of range."
