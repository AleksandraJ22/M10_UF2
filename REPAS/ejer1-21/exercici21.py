

numeros  = input('Posa 10 numeros: ')

lista_numeros = numeros.split()

print(lista_numeros)

suma = int(sum(lista_numeros))

    
mitjana = suma / len(lista_numeros)


lista_numeros.append(suma)
lista_numeros.append(mitjana)


print('Numeros del usuari: ', lista_numeros)
print('suma total: ',suma)
print('mitjana: ',mitjana)