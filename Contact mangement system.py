contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    print(f"Contact {name} added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print("-" * 20)

def search_contact(name):
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")
    else:
        print(f"Contact {name} not found.")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        print(f"Contact {name} updated successfully.")
    else:
        print(f"Contact {name} not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def contact_management_system():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = int(input("Enter your choice (1-6): "))
        
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == 4:
            name = input("Enter name to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email address (leave blank to skip): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == 5:
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == 6:
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_management_system() 