from ..models.connection import cursor
from contextlib import closing
from ..util import row_to_dict, rows_to_dict

class Doador():
    def getAll():
        with closing(cursor()) as con, closing(con.cursor()) as cur:
            cur.execute("SELECT * FROM Doadores")
            return rows_to_dict(cur.description, cur.fetchall())
        
    def create(doador):
        with closing(cursor()) as con, closing(con.cursor()) as cur:
            cur.execute("INSERT INTO Doadores (Nome, Sobrenome, Cidade, País, Valor) VALUES (%s, %s, %s, %s, %s)", [
                doador['nome'], doador['sobrenome'], doador['cidade'], doador['pais'], doador['valor'],])
            doador = cur.lastrowid
            con.commit()
            con.close()
            return doador
        