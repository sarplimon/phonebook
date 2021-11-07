from replit import db 

def add_contact(name, phone_number):
    if name in db:
        print("Name already exists")
    else:
        db[name] = phone_number

def get_contact(name):
    number = db.get(name)
    return number

def search_contacts(search):
    match_keys = db.prefix(search)
    return {k: db[k] for k in match_keys}

def update_number(old_name, new_number):
    db[old_name] = new_number

def update_contact(old_name, new_name, new_number):
    db[new_name] = new_number
    del db[old_name]

def delete_contact(name):
    del db[name]


