import psycopg2

def conectar_bd():
    try:
        conn = psycopg2.connect(
            dbname="sistema_agua",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        print("Conexión exitosa a la base de datos.")
        return conn
    except Exception as e:
        print("Error conectando a la BD:", e)
        return None


