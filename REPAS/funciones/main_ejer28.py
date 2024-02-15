from exercici28 import mostrarNumeroAleatori


def main():
    num1=int(input('Inserta un numero: '))
    num2 =int(input('Inserta otro numero: '))
    if num1 > num2:
        extra = num1
        num1=num2
        num2 = extra
   
        
    print(mostrarNumeroAleatori(num1, num2))
   
        
    
    
    
    
  
    

if __name__ == '__main__':
    main()
   


