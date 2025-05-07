# 📒 Contact Book

A simple command-line Contact Book application built with Python that allows users to manage contacts by adding, viewing, updating, searching, and deleting contact details.

---

## 🧠 Description

- ➕ Add new contacts with name, phone number, and email.
- 📋 View all saved contacts in a clear format.
- ✏️ Update phone or email of existing contacts.
- 🔍 Search for contacts by name.
- ❌ Delete contacts from the list.
- 🧹 Automatically clears the screen between actions for better readability (optional).

---

## 💻 How It Works

1. **User selects an option** from the main menu.
2. Based on the selection, the app:
   - Adds a new contact
   - Displays all saved contacts
   - Updates an existing contact
   - Searches for a specific contact
   - Deletes a contact
   - Or exits the application
3. The screen clears after each operation to provide a clean user interface (on both Windows and Unix systems).

---

## 📂 Code Structure

### `clear_screen()`
Clears the terminal/console screen based on the operating system.

### `main_menu()`
Displays the list of options available to the user.

### Contact Operations:
- `add_contact(contacts)`
- `view_contacts(contacts)`
- `update_contact(contacts)`
- `search_contact(contacts)`
- `delete_contact(contacts)`

### `main()`
Main loop to handle user interaction and coordinate the app flow.

---

## 🚀 Getting Started

To run the app:

1. Ensure **Python 3** is installed.
2. Save the code in a file named `contact_book.py`.
3. Run the script using:

```bash
python contact_book.py
```

---

## 📧 Author

Created with ❤️ to help new Python programmers build useful tools while mastering core programming concepts.

---
