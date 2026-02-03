contacts = {'ahmed':'01123456', 'noor':'01213456' ,'nada':'01234561'}
print(contacts.keys())
key= input('enter the name: ').lower()
value = contacts.get(key,'not found')
print(f'the value for {key} is:{value}')