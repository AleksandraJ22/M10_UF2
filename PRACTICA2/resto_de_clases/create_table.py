
from connection import *


#creamos la query 

sql = """ CREATE TABLE USERS(
    user_id SERIAL PRIMARY KEY, 
    user_name VARCHAR(255) NOT NULL, 
   user_surname VARCHAR(255) NOT NULL, 
    user_age BIGINT NOT NULL, 
    user_email VARCHAR(255) NOT NULL,
    user_dni VARCHAR(255) NOT NULL
 
    
    
    )"""
    
    
print(sql)
    #ejecutamos la query 
connection.execute(sql)
print(connection)
conn.commit() #para realizar los cambios 