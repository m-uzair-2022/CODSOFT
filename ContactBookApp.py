# Contact Book Application
# Stores and manages contact details using CLI

contacts = []  # List to store contacts

# Function to display menu
def show_menu():
    print("\n_______________________________________")
    print("            Contact Book              ")
    print("_______________________________________")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    for i, c in enumerate(contacts, start=1):
        print(f"\n{i}. Name  : {c['name']}")
        print(f"   Phone : {c['phone']}")

# Function to search contact
def search_contact():
    search = input("Enter name or phone to search: ")

    for c in contacts:
        if search == c['name'] or search == c['phone']:
            print("\nContact Found:")
            print("Name   :", c['name'])
            print("Phone  :", c['phone'])
            print("Email  :", c['email'])
            print("Address:", c['address'])
            return

    print("Contact not found.")

# Function to update contact
def update_contact():
    view_contacts()
    if not contacts:
        return

    try:
        choice = int(input("Enter contact number to update: "))
        if 1 <= choice <= len(contacts):
            c = contacts[choice - 1]
            c['name'] = input("Enter New Name: ")
            c['phone'] = input("Enter New Phone: ")
            c['email'] = input("Enter New Email: ")
            c['address'] = input("Enter New Address: ")
            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete contact
def delete_contact():
    view_contacts()
    if not contacts:
        return

    try:
        choice = int(input("Enter contact number to delete: "))
        if 1 <= choice <= len(contacts):
            contacts.pop(choice - 1)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("_______________________________________")
        print("     Exiting Contact Book. Goodbye!    ")
        print("_______________________________________")
        break
    else:
        print("Invalid choice. Please select 1 to 6.")
