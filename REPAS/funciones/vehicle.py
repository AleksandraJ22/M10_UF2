


class Vehicle:
    
    
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
        
      
    def parts():
        
        print('Atributos: '+ '\n')
        print('Marca: {marca}, Model: {model}, Any: {any}, Matricula: {matricula}, Places: {places}, Kilometros: {kilometros}')
        
     
    
    v1 = Vehicle('nissan','nissan 2X','2010','FDGFBFB3232', '6', '10000')
    v1.parts()
        
        
        
        
        
    
    
        
    
   
        
    