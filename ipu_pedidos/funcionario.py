import db_connect

def todos_funcionarios():
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute('SELECT * FROM funcionario;')
        resultado = cursor.fetchall()
        return resultado
    except Exception as e :
        print(e)
    finally:
        db_connect.db_close_connection(connection)

def update_funcionario(nome, idfuncionario):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("UPDATE funcionario SET nome = %s WHERE idfuncionario = %s;",(nome,idfuncionario))
        connection.commit()
        print("Funcionario atualizado com sucesso.")
    except Exception as e:
        print("Erro ao atualizar",e)
    finally:
        db_connect.db_close_connection(connection)

def delete_funcionario(idfuncionario):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("DELETE FROM funcionario WHERE idfuncionario = %s;",(idfuncionario,))
        connection.commit()
        print("Funcionario deletado com sucesso.")
    except Exception as e:
        print("Erro ao deletar",e)
    finally:
        db_connect.db_close_connection(connection)

def insert_funcionario(nome,cpf):
    try:
        connection = db_connect.db_open_connection()

        cursor = connection.cursor()
        cursor.execute("INSERT INTO funcionario (nome,cpf) VALUES (%s,%s)", (nome,cpf))
        connection.commit()
        cursor.close()
        connection.close()
        print("Funcionario inserido com sucesso")
    except Exception as e:
        print("Erro ao inserir funcionario",e)
    finally:
        db_connect.db_close_connection
