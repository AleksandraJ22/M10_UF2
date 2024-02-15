
import json

class user():
    
    def __init__(self, nom, cognom, anys, gmail, adreça, dni):
        self.nom=nom
        self.cognom=cognom
        self.anys=anys
        self.gmail=gmail
        self.adreça=adreça
        self.dni=dni 
        
        
    def getNom(self):
        return self.nom
    def setNom(self, nom):
        self.nom=nom
        
    
    def getCognom(self):
        return self.cognom
    def setCognom(self, cognom):
        self.cognom=cognom 
        
        
    def getAnys(self):
        return self.anys
    def setAny(self, anys):
        self.anys=anys
        
        
    def getGmail(self):
        return self.gmail
    def setGmail(self, gmail):
        self.gmail=gmail
        
        
    def getAdreça(self):
        return self.adreça
    def setPlaces(self, adreça):
        self.adreça=adreça
        
        
    def getDni(self):
        return self.dni
    def setKilometros(self, dni):
        self.dni=dni
        
      
    def salutacio(self):
        
        
        print(f'Nom: {self.nom}, Cognom: {self.cognom}, Any: {self.anys}, Gmail: {self.gmail}, Adreça: {self.adreça}, Dni: {self.dni}')
        
        
        
        
    def to_dict(self):
         
         dict_user = { 
                        'nom':self.nom,
                        'cognom':self.cognom,
                        'anys':self.anys,
                        'gmail':self.gmail,
                        'adreça':self.adreça,
                        'dni':self.dni
             
         }
         with open("user.json", "w") as file:
            json.dump(dict_user,file)
            
            
    def LeerJSON(self):
        with open('user.json', 'r') as file:
            result = json.load(file)
            print(result)
        
        
         
         
         





        
    
    
        
    
   
        
    