from exercici31  import totalFactura



def main():
    
    cant = float(input('Introduce cantidad sin iva: '))
    iva = int(input('Introduce iva a aplicar: '))
    
    if iva == 0 or iva == 4 or iva == 10 or iva == 21:
        iva = 21
    
    print(cant, '->Valor sin iva')
    print(iva, '-> iva')
    
    
    resultado = totalFactura(cant,iva)
    print(resultado,'->valor con iva')
    
if __name__ == '__main__':
    main()


    