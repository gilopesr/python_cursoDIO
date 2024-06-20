import sqlite3
from pathlib import Path

ROOTH_PATH = Path (__file__).parent 

conexao = sqlite3.connect(ROOTH_PATH / 'meu_banco.sqlite')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?)', ('teste 2', 'teste2@gmail.com'))
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?,?,?)', (2, 'teste3', 'teste3@gmail.com'))
    conexao.commit()
except Exception as exc:
    print(f'OPS! um errro aconteceu {exc}')
    conexao.rollback()
finally:
    conexao.commit()