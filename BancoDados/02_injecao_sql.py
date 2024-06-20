import sqlite3
from pathlib import Path

ROOTH_PATH = Path (__file__).parent 

conexao = sqlite3.connect(ROOTH_PATH / 'meu_banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input('insira o id do cliente: ')
cursor.execute(f'select * from clientes where id={id_cliente}')
cliente = cursor.fetchone()
print(dict(cliente))