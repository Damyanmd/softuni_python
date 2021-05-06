contact = input()
phonebook = {}
while not contact.isdigit():
    name, phone = contact.split('-')
    phonebook[name] = phone
    contact = input()

n = int(contact)
for i in range(n):
    contact = input()
    if contact in phonebook:
        for (key, value) in phonebook.items():
            if contact in key:
                print(f'{key} -> {value}')
    else:
        print(f'Contact {contact} does not exist.')