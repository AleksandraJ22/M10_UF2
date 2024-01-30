import psycopg2

conexio = psycopg2.connect(
    
    database = "postgres",
    user='user_postgres',
    password='pass_postgres',
    host='localhost',
    port='5432'
    
    
)


connection = conexio.cursor()

print(connection)



