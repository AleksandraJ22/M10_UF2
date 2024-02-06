from connection import hacerConexion
#insertar un registro a la tabla 


def creatRegistro():
    sql= """INSERT INTO USERS(user_id, user_name, user_surname, user_age, user_email, user_dni) 
VALUES ('1', 'Ana','Martinez', 30, 'anaMartinez@gmail.com', '24344443B')

    
    
    """
  
    variable = hacerConexion()
    variable.execute(sql)
    variable.commit()



