from exercici29 import mostrarNumeros



def main():
    num1=int(input('Inserta un numero: '))
    num2 =int(input('Inserta otro numero: '))
    print('Los numeros que hay entre ellos son:')
    mostrarNumeros(num1,num2)
    

if __name__ == '__main__':
    main()