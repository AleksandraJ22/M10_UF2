

from vehicle import *


def main():
    v1 = Vehicle('nissan','nissan 2X','2010','FDGFBFB3232', '6', '10000')
    v1.to_dict()
    print('Atributos:\n')
    v1.parts()
    
    print('Atributos en forma JSON: \n')
    v1.LeerJSON()
   
    
    

if __name__ == '__main__':
    main()
   
    
    
    