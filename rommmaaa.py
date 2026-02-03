contacts = {'ahmed':'01123456', 'noor':'01213456' ,'nada':'01234561'}
print(contacts.keys())
search_name = input('enter the name: ')
if search_name in contacts:
    print(f'found {search_name}')
    print(f'phone number:{contacts[search_name]}')
else:
    print(f'sorry,{search_name}is not in the contact book')