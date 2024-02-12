


contactes = {'Roger':'678232311', 'Oriol':'566879326'}

def elimina(contactes, user):
    del contactes[user]
    return contactes[user]

print(elimina(contactes, 'Pablo'))


