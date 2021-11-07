import contacts
from os import system

main_message = """WELCOME TO PHONEBOOK
----------------------------------
Please choose:
1 - to add a new contact
2 - to find a contact
3 - to update a contact
4 - to delete a contact
----------------------------------
"""

def prompt_add_contact():
    name = input("Please enter the contact's name: ")
    number = input("Please enter the contact's phone number: ")
    print(f"Adding {name} with {number}")
    contacts.add_contact(name, number)

def prompt_get_contact():
    name = input("Please enter the name to find: ")
    number = contacts.get_contact(name)
    if number:
        print(f"{name}'s number is {number}")
    else:
        matches = contacts.search_contacts(name)
        if matches:
            for k in matches:
                print(f"{k}'s number is {matches[k]}")
        else:
            print(f"It looks like {name} does not exist")

def prompt_update_contact():
    old_name = input("Please enter the name of the contact to update: ")
    old_number = contacts.get_contact(old_name)
    if old_number:
        new_name = input(f"Please enter the new name for this contact (leave blank to keep {old_name}): ").strip()
        new_number = input(f"Please enter the new number for this contact (leave blank to keep {old_number}): ").strip()

        if not new_number:
            new_number = old_number

        if not new_name:
            contacts.update_number(old_name, new_number)
        else:
            contacts.update_contact(old_name, new_name, new_number)
    else:
        print(f"It looks like {old_name} does not exist")

def prompt_delete_contact():
    name = input("Please enter the name to delete: ")
    contact = contacts.get_contact(name)
    if contact:
        print(f"Deleting {name}")
        contacts.delete_contact(name)
    else:
        print(f"It looks like {name} does not exist")



def main():
    print(main_message)
    choice = input("Please make your choice: ").strip()
    if choice == "1":
        prompt_add_contact()
    elif choice == "2":
        prompt_get_contact()
    elif choice == "3":
        prompt_update_contact()
    elif choice == "4":
        prompt_delete_contact()
    else:
        print("Invalid input. Please try again.")

while True:
    system('clear')
    main()
    input("Press enter to continue: ")