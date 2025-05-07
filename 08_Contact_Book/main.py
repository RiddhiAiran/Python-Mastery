# Contact Book 
# Description: A simple command-line contact book application that allows users to add, view, update, search, and delete contacts.
# clear_screen function: Clears the console screen for better readability (optional but recommended).

def clear_screen():
    ''' Clear the console screen. '''
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    print("Welcome to the Contact Book!")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Search Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact(contacts):
    ''' Add a new contact to the contact book. '''
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"Contact {name} added successfully.")

def view_contacts(contacts):
    ''' View all contacts in the contact book. '''
    if not contacts:
        print("No contacts found.")
        return
    print("Contacts:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def update_contact(contacts):
    ''' Update an existing contact in the contact book. '''
    name = input("Enter the name of the contact to update: ")
    if name not in contacts:
        print(f"Contact {name} not found.")
        return
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    print(f"Contact {name} updated successfully.")

def search_contact(contacts):
    ''' Search for a contact in the contact book. '''
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Contact found: Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print(f"Contact {name} not found.")

def delete_contact(contacts):
    ''' Delete a contact from the contact book. '''
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")

def main():
    clear_screen()
    contacts = {}
    while True:
        main_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact(contacts)
            continues = input("press any key to continue...")
            clear_screen()
        elif choice == '2':
            view_contacts(contacts)
            continues = input("press any key to continue...")
            clear_screen()
        elif choice == '3':
            update_contact(contacts)
            continues = input("press any key to continue...")
            clear_screen()
        elif choice == '4':
            search_contact(contacts)
            continues = input("press any key to continue...")
            clear_screen()
        elif choice == '5':
            delete_contact(contacts)
            continues = input("press any key to continue...")
            clear_screen()
        elif choice == '6':
            print("Exiting the Contact Book. Goodbye!")
            continues = input("press any key to continue...")
            clear_screen()
            break
        else:
            print("Invalid choice. Please try again.") 
            continues = input("press any key to continue...")
            clear_screen()

if __name__ == "__main__":
    main()