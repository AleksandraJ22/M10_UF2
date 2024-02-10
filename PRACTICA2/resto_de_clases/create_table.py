
from connection import hacerConexion


#creamos la query 


def createTable():
    sql = """ CREATE TABLE USERS(
    user_id SERIAL PRIMARY KEY, 
    user_name VARCHAR(255) NOT NULL, 
   user_surname VARCHAR(255) NOT NULL, 
    user_age BIGINT NOT NULL, 
    user_email VARCHAR(255) NOT NULL,
    user_dni VARCHAR(255) UNIQUE NOT NULL
 
    
    
    )"""
    
    print(sql)
    variable = hacerConexion()
        #ejecutamos la query 
    variable.execute(sql)
    print(variable)
    #variable.commit() #para realizar los cambios 
    print('Se ha creado correctamente')
    
