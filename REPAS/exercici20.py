






diccionario = {}
lista = []

cant = int(input('Cuantos contactos vas a poner? '))
for i in range(cant):
    contacte = input()
    lista = contacte.split()
    diccionario[lista[0]] = lista[1]
    diccionario.get(lista[0],'No se puede repetir')
    

print(diccionario)






