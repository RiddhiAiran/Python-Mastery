# Shopping List App
# Description: A simple shopping list application that allows users to add, remove, clear, and view items in their shopping list.

# Step 1: Initialize the Shopping List
shopping_list = []

# Step 2: Define Functions for Shopping List Operations
def add_item(item):
    """Add an item to the shopping list."""
    shopping_list.append(item)
    print(f"\n✅ Added '{item}' to the shopping list.")

def remove_item(item):
    """Remove an item from the shopping list."""
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n❌ Removed '{item}' from the shopping list.")
    else:
        print(f"\n⚠️ '{item}' is not in the shopping list.")

def clear_list():
    """Clear the shopping list."""
    shopping_list.clear()
    print("\n🧹 Cleared the shopping list.")

def view_list():
    """View the items in the shopping list."""
    print("\n📝 Shopping List:")
    if shopping_list:
        for i, item in enumerate(shopping_list, start=1):
            print(f"  {i}. {item}")
    else:
        print("  (The shopping list is empty.)")

# Step 3: Main Function to Run the Shopping List App
def shopping_list_app():
    """Run the shopping list application."""
    print("=" * 40)
    print("🛒 Welcome to the Shopping List App! 🛍️")
    print("=" * 40)

    while True:
        print("\nMenu:")
        print("  1. ➕ Add Item")
        print("  2. ➖ Remove Item")
        print("  3. 🧹 Clear List")
        print("  4. 📋 View List")
        print("  5. ❌ Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            add_item(item)
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            remove_item(item)
        elif choice == '3':
            clear_list()
        elif choice == '4':
            view_list()
        elif choice == '5':
            print("\n👋🏼 Exiting the Shopping List App. Goodbye!")
            print("=" * 40)
            break
        else:
            print("\n❗ Invalid choice. Please enter a number from 1 to 5.")

# Step 4: Run the Shopping List App
if __name__ == "__main__":
    shopping_list_app()
