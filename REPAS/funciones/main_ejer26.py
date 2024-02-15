from user import *



def main():
    user1 = user('nil','martinez','20','nilmartinez334@gmail.com', 'calle 123, Barcelona', '21324244G')
    user1.to_dict()
   
    user1.salutacio()
    
    print('Atributos en forma JSON: \n')
    user1.LeerJSON()
   
    
    

if __name__ == '__main__':
    main()
   
    
    