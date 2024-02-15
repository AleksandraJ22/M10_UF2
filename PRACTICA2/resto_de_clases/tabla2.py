from connection import hacerConexion


def crearUsuarios2():
    try:
        sql ="""CREATE TABLE USERS2(
        
    user_id2 SERIAL PRIMARY KEY, 
    user_name2 VARCHAR(255) NOT NULL, 
   user_surname2 VARCHAR(255) NOT NULL, 
    user_age2 BIGINT NOT NULL, 
    user_email2 VARCHAR(255) NOT NULL,
    user_dni2 VARCHAR(255) UNIQUE NOT NULL
 
    
    )
        """
        variable = hacerConexion()
        variable.execute(sql)
        
        variable.commit()
    except (Exception) as error:
        print("Error",error)
    finally:
        variable.close()
    
    
    

    
  