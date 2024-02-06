from connection import hacerConexion

def funcionDelete():
    sql= """ DELETE FROM public.USERS where user_id = 1"""
    variable = hacerConexion()
    #ejecutamos la query 
    variable.execute(sql)
    #nos aseguramos que se afectuen los cambios
    variable.commit()
    print('Eliminado correctamente')
    

