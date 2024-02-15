def amb_iva(ftotal, iva = 21):
    ftotal = ftotal * (1+(iva/100)) 
    return ftotal 


ftotal = float(input('Introdueix el preu de tot el carrito: '))

print(amb_iva(ftotal, 21))

