import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

server=os.getenv('DB_SERVER')
db=os.getenv('DB_DATABASE')
username=os.getenv('DB_USER')
password=os.getenv('DB_PASSWORD')

conexao = pyodbc.connect(driver='{SQL Server}', host=server, database=db,
                      user=username, password=password)

print("Conexao Bem Sucedida")

cursor = conexao.cursor()
