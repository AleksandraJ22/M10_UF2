from connection import hacerConexion

def funcionREAD():
    sql = """ SELECT  user_id , 
    user_name, 
   user_surname, 
    user_age , 
    user_email ,
    user_dni FROM public.USERS"""
    variable = hacerConexion()
         
    variable.execute(sql)

    result = variable.fetchall() #nos devuelve los resultados en forma de lista 
    
    for i in result:
        print("user_id: ",i[0],)
        print("user_name: ",i[1],)
        print("user_surname: ",i[2],)
        print("user_age: ",i[3],)
        print("user_email: ",i[4],)
        print("user_dni: ",i[5],)
    
    
    