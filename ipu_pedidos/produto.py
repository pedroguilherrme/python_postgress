import db_connect

def todos_produtos():
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute ('SELECT * FROM produto;')
        resultado = cursor.fetchall()
        return resultado
    except Exception as e :
        print(e)
    finally:
        db_connect.db_close_connection(connection)

def delete_produto(idproduto):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("DELETE FROM produto WHERE idproduto = %s;",(idproduto,))
        connection.commit()
        print("Produto deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar",e)
    finally:
        db_connect.db_close_connection(connection)

def todos_produtos():
    try:
        connection = db_connect.db_open_connection()
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM produto;")
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        db_connect.db_close_connection(connection)

def insert_produto(nome,valor):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("INSERT INTO produto (nome,valor) VALUES (%s,%s)", (nome,valor))
        connection.commit()
        cursor.close()
        connection.close()
        print("Produto inserido com sucesso")
    except Exception as e:
        print("Erro ao inserir produto",e)
    finally:
        db_connect.db_close_connection

    
def update_produto(valor, idcliente):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("UPDATE produto SET valor = %s WHERE idproduto = %s;",(valor,idcliente))
        connection.commit()
        print("Produto atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar",e)
    finally:
        db_connect.db_close_connection(connection)


