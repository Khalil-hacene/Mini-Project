# Contact Book

contacts = {}

def add_contacts(contacts):
    name = input("Enter the name: ")
    number = input("Enter the phone number: ")
    contacts[name] = number
    print("✅ Contact added!")

def delete_contacts(contacts):
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ '{name}' deleted from contacts.")
    else:
        print("❌ Contact not found.")

def show_contacts(contacts):
    print("\n📒 Contact List:")
    if not contacts:
        print("No contacts available.")
    else:
        for name, number in contacts.items():
            print(f"{name}: {number}")
    print()

def main():
        while True:
            print("------Contact Book-------")
            print("1- Add contact")
            print("2- Delete Contact")
            print("3- Contact List")
            print("4- Exit")
            print("-------------------------")
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid Input")
                continue

            if choice == 1:
                    add_contacts(contacts)
            elif choice == 2:
                    delete_contacts(contacts)
            elif choice == 3:
                    show_contacts(contacts)
            elif choice == 4:
                print("👋 Thank you for using our services!")
                break 
            else:
                print("❗ Invalid choice. Please select from the menu.")
main()