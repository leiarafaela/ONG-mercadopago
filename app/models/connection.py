import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-T2JV7P5;"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()