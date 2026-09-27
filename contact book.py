"""
Assignment 1: Contact Book using Dictionary
Add, search, update, delete contacts.
"""

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print(f"Contact '{name}' already exists. Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")


def search_contact():
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"  Phone: {contact['phone']}")
        print(f"  Email: {contact['email']}")
    else:
        print(f"No contact found with name '{name}'.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print(f"No contact found with name '{name}'.")
        return
    phone = input(f"Enter new phone (leave blank to keep '{contacts[name]['phone']}'): ").strip()
    email = input(f"Enter new email (leave blank to keep '{contacts[name]['email']}'): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print(f"Contact '{name}' updated successfully.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with name '{name}'.")


def list_contacts():
    if not contacts:
        print("No contacts saved yet.")
        return
    for name, info in contacts.items():
        print(f"{name}: {info['phone']} | {info['email']}")


def main():
    menu = """
--- Contact Book ---
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. List All Contacts
6. Exit
"""
    actions = {
        "1": add_contact,
        "2": search_contact,
        "3": update_contact,
        "4": delete_contact,
        "5": list_contacts,
    }

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()
        if choice == "6":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
