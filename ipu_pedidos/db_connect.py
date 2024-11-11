import psycopg2
import traceback

def db_open_connection():
    try:
        conn = psycopg2.connect(database = "ipu_entregas", host = "localhost", user = "postgres", password = "pg19102002", port = "5432")
        conn.autocommit = True
        print("Conexão com o banco ipu_entregas bem sucedida!")
        return conn
    except Exception as e:
        backtrace = traceback.format_exc()
        print(f"Ocorreu o seguinte erro ao conectar no banco ipu_entregas: {str(e)}")
        print(f"Backtrace: {backtrace}")

def db_close_connection(connection):
    if connection:
        connection.close()
        print("Conexão com o banco ipu_entregas finalizada com sucesso!")
    else:
        raise Exception("Impossível finalizar conexão com o banco ipu_entregas. Você precisa passar uma conexão válida como argumento.")