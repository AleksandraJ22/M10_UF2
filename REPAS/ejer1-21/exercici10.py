
import random
num = random.randint(1,100)


encertado = False


valor = int(input('Introdueix un num: '))

contador = 0

while(valor!=num):
    
    
    
    
    if valor < num:
        print('El numero a adivinar es mas grande')
        
        
        
    else:
        print('El numero a adivinar es mas pequeño')
        #valor = input('Introduce otro numero: ')
      
        
        
    valor = int(input('Introduce otro numero: '))
    contador = contador +1
        

        
        
print('Has encertado el numero! Tus intentos son:',contador)
   
        
        
        
        

        
    
    
    





