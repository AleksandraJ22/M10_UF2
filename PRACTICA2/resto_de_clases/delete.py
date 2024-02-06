from connection import *


sql= """ DELETE FROM public.USERS where user_id = 1"""

#ejecutamos la query 
connection.execute(sql)
#nos aseguramos que se afectuen los cambios
conn.commit()