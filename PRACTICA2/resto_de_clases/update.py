from connection import hacerConexion

def metodoUpdate():
    sql = """  UPDATE public.USERS SET user_name='Anastasia' WHERE user_id=1 """
    variable = hacerConexion()
    variable.execute(sql)
    variable.commit()
    result = variable.rowcount
    print("id modificada ",result, "Actualizacion afectuada sin errores")