
import json

class Vehicle():
    
    def __init__(self, marca, model, any, matricula, places, kilometros):
        self.marca=marca
        self.model=model
        self.any=any
        self.matricula=matricula
        self.places=places
        self.kilometros=kilometros 
        
        
    def getMarca(self):
        return self.marca
    def setMarca(self, marca):
        self.marca=marca
        
    
    def getModel(self):
        return self.model
    def setModel(self, model):
        self.model=model 
        
        
    def getAny(self):
        return self.any
    def setAny(self, any):
        self.any=any
        
        
    def getMatricula(self):
        return self.matricula
    def setMatricula(self, matricula):
        self.matricula=matricula
        
        
    def getPlaces(self):
        return self.places
    def setPlaces(self, places):
        self.places=places
        
        
    def getKilometros(self):
        return self.kilometros
    def setKilometros(self, kilometros):
        self.kilometros=kilometros
        
      
    def parts(self):
        
        print(f'Marca: {self.marca}, Model: {self.model}, Any: {self.any}, Matricula: {self.matricula}, Places: {self.places}, Kilometros: {self.kilometros}')
        
        
        
        
    def to_dict(self):
        
        
      
        
        diccionario = { 
                        'marca':self.marca,
                        'model':self.model,
                        'any':self.any,
                        'matricula':self.matricula,
                        'places':self.places,
                        'kilometros':self.kilometros
             
         }
        with open("vehicle.json", "w") as file:
            json.dump(diccionario,file)
            
            
    def LeerJSON(self):
        with open('vehicle.json', 'r') as file:
            result = json.load(file)
            print(result)
        
        
         
         
         





        
    
    
        
    
   
        
    