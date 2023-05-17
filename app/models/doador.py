from ..models.connection import conexao
from contextlib import closing
from ..util import row_to_dict, rows_to_dict
import pyodbc


class Doador():
    def getAll():
        pass
        
    def create(doador):
        try:

            # Abrir uma nova conexão com o banco de dados
            cursor = conexao.cursor()
            
            # Execução do comando SQL
            cursor.execute("INSERT INTO Doadores (Nome, Sobrenome, Cidade, País, Valor) VALUES (?, ?, ?, ?, ?)", [doador['nome'], doador['sobrenome'], doador['cidade'], doador['pais'], doador['valor'],])
            # Confirma a transação
            conexao.commit()
            print("Objeto criado e salvo com sucesso!")

        except pyodbc.Error as erro:
        # Em caso de erro, desfazer as alterações
            conexao.rollback()
            print(f"Ocorreu um erro ao criar e salvar o objeto: {erro}")

        finally:
            # Fechar a conexão com o banco de dados
            cursor.close()

        return doador