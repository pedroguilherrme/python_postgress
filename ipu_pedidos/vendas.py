import db_connect

def todas_vendas():
    try:
        connection = db_connect.db_open_connection()
        
        cursor = connection.cursor()
        cursor.execute('SELECT idvenda, fnc.nome, pdt.nome,vnd.valor ,data_venda FROM vendas as vnd left outer join funcionario as fnc on\
                        fnc.idfuncionario = vnd.idfuncionario\
                        left outer join produto as pdt on pdt.idproduto = vnd.idproduto ;')
        resultado = cursor.fetchall()
        return resultado
    except Exception as e:
        print(e)
    finally:
        db_connect.db_close_connection(connection)


def insert_venda(idfuncionario,valor,idproduto):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("INSERT INTO vendas (idfuncionario,valor,idproduto) VALUES (%s,%s,%s)", (idfuncionario,valor,idproduto))
        connection.commit()
        cursor.close()
        connection.close()
        print("Venda inserida com sucesso")
    except Exception as e:
        print("Erro ao inserir venda",e)
    finally:
        db_connect.db_close_connection

def delete_venda(idvenda):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("DELETE FROM vendas WHERE idvenda = %s;",(idvenda,))
        connection.commit()
        print("Venda deletada com sucesso.")
    except Exception as e:
        print("Erro ao deletar",e)
    finally:
        db_connect.db_close_connection(connection)

def update_vendas(valor, idvenda):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("UPDATE vendas SET valor = %s WHERE idvenda = %s;",(valor,idvenda))
        connection.commit()
        print("Venda atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar",e)
    finally:
        db_connect.db_close_connection(connection)