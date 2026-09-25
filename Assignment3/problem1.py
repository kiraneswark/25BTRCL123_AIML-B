contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        print("\nContacts:")

        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])

    elif choice == "3":
        search = input("Enter name to search: ")

        for contact in contacts:
            if contact["name"] == search:
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
        
 ##sample output
        # 1. Add Contact
#       2. View Contacts
#3. Search Contact
#4. Exit

#Enter your choice: 1
#Enter name: Rahul
#Enter phone number: 9876543210
#Contact added successfully!