contacts = {}



class contact:

    def __init__(self,contacts):
        self.contacts=contacts


    def add_contact(self):
        name = input("Enter the contact's name: ")
        phone_number = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        contacts[name] = {
            'Phone': phone_number,
            'Email': email,

        }
        print(f"{name} is added in your contacts.")
    def view_contacts(self):


        if not contacts:
              print("No contacts found.")
        else:
              print("Contact List:")
        for name, info in contacts.items():
              print(f"Name: {name}")
              print(f"Phone: {info['Phone']}")
              print(f"Email: {info['Email']}")




    def search_contact(self):
         search_term = input("Enter a name or phone number to search: ")
         found = False
         for name, info in contacts.items():
          if search_term in name or search_term == info['Phone']:
             print(f"Name: {name}")
             print(f"Phone: {info['Phone']}")
             print(f"Email: {info['Email']}")

             found = True
          if not found:
             print("Contact not found.")


# Function to update contact details
    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in contacts:
          print("Current Contact Information:")
          print(f"Name: {name}")
          print(f"Phone: {contacts[name]['Phone']}")
          print(f"Email: {contacts[name]['Email']}")

          print('-' * 20)
          contacts[name]['Phone'] = input("Enter the new phone number (press Enter to keep it unchanged): ") or \
                                  contacts[name]['Phone']
          contacts[name]['Email'] = input("Enter the new email address (press Enter to keep it unchanged): ") or \
                                  contacts[name]['Email']

          print(f"{name}'s contacts information has been updated from your contact.")
        else:
          print("Contact not found.")


    def delete_contact(self):
       name = input("Enter the name of the contact to delete: ")
       if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.")
       else:
           print("Contact not found.")


while True:
    print("\nContact Book:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
         contact.add_contact(self=contacts)
    elif choice == '2':
         contact.view_contacts(self=contact)
    elif choice == '3':
        contact.search_contact(self=contact)
    elif choice == '4':
        contact.update_contact(self=contact)
    elif choice == '5':
        contact.delete_contact(self=contact)
    elif choice == '6':
        print("Exiting the contact management program.")
        break
    else:
        print("Invalid choice. Please try again.")