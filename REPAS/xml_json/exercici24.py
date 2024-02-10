

import json

def funcionLeerJSON():
    with open('ejercicio23.json', 'r') as file:
        result = json.load(file)
        print(result)
        
        

        
        
        