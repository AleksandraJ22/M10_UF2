

value = int(input('Introduce un numero entre 10 y 100: '))

lista=[]


for i in range(value):
    lista.append(i+1)
    
    
    
myTupla=tuple(lista)
    
    
print(myTupla)