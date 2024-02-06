from connection import *


sql = """  UPDATE public.USERS SET user_name='Anastasia' WHERE user_id=1 """


connection.execute(sql)
conn.commit()
result = connection.rowcount
print("id modificada ",result, "Actualizacion afectuada sin errores")