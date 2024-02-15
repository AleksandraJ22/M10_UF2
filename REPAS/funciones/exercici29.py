

def mostrarNumeros(num1,num2):
    
    suma = 0
    
    for x in range(num1+1,num2):
        suma = suma + x
        print(x)
        
    print('La suma es', suma)