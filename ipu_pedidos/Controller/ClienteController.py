import db_connect

def insert_cliente(nome,cpf,genero):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("INSERT INTO cliente (nome,cpf,genero) VALUES (%s,%s,%s)", (nome,cpf,genero))
        connection.commit()
        cursor.close()
        connection.close()
        print("Cliente inserido com sucesso")
    except Exception as e:
        print("Erro ao inserir cliente",e)
    finally:
        db_connect.db_close_connection

def todos_clientes():
    try:
        connection = db_connect.db_open_connection()
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM cliente;")
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        db_connect.db_close_connection(connection)
