import json 

datas={
    "book":[{
        
        "titol":"Harry Potter",
            "cover":"blando",
                "year":"2000",
                "pages":"500"
    },
        {
        
        "titol":"Harry Potter 2",
            "cover":"blando",
                "year":"2001",
                "pages":"1000"
    },
        {
        
        "titol":"Harry Potter 3",
            "cover":"blando",
                "year":"2003",
                "pages":"500"
    },
        {
        
        "titol":"Harry Potter 4",
            "cover":"blando",
                "year":"2000",
                "pages":"500"
    },    
        
    ]
    
    
}
def funcion():
    with open("ejercicio23.json", "w") as file:
        json.dump(datas,file)
        
        
        #ejercicio 24 
def funcionLeerJSON():
    print(json.dumps(datas,indent=2))
    
             
        
funcion()
funcionLeerJSON()
        
        