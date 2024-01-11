
import random
num = random.randint(1,100)

contador = 0
encertado = False
valor = input('Introdueix un num: ')
contador=contador+1


while(encertado):
    if {valor} == {num}:
        print('Muy bien! intentos: ',contador)
        encertado=True
    
    elif {valor} > {num}:
        valor=input('El numero a adivinar es mas pequeño, introduce un numero: ')
        contador = contador +1
    else:
        valor=input('El numero a adivinar es mas grande, introduce un numero: ')
        contador = contador +1
        

        
    
    
    





