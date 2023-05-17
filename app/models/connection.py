import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=vsinfo.net,14337;"
    "Database=ibooks;"
    "Username=user_ibooks"
    "Password=3w#94D*X"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()