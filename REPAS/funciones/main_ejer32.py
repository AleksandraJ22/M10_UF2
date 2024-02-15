
from exercici32 import llistaQuadrats


def main():
    print('Introdueix 10 numeros: ')
  
    lista = []
    for x in range(10):
        num = int(input(f'num {x+1}: '))
        lista.append(num)
        
    
    
    

    
    print(llistaQuadrats(lista))
    
    
        
        
if __name__ == '__main__':
    main()

