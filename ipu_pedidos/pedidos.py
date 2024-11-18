import db_connect

def todos_pedidos():
    try:
        connection = db_connect.db_open_connection()
        
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pedidos;")
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        db_connect.db_close_connection(connection)


def insert_pedido(nome_produto,nome_cliente):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("INSERT INTO pedidos (nome_produto, nome_cliente) VALUES (%s,%s)", (nome_produto,nome_cliente))
        connection.commit()
        cursor.close()
        connection.close()
        print("Pedido inserido com sucesso")
    except Exception as e:
        print("Erro ao inserir cliente",e)
    finally:
        db_connect.db_close_connection

def delete_pedido(idpedido):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("DELETE FROM pedidos WHERE idpedido = %s;",(idpedido,))
        connection.commit()
        print("Pedido deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar",e)
    finally:
        db_connect.db_close_connection(connection)
def update_pedido(idpedido,nome_produto):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("UPDATE pedidos SET nome_produto = %s WHERE idpedido = %s;",(idpedido,nome_produto))
        connection.commit()
        print("Pedido atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar",e)
    finally:
        db_connect.db_close_connection(connection)


