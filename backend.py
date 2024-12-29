import sqlite3

def connect():
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY, nome text, sobrenome text, email text, cpf text)")
        conn.commit()

def insert(nome, sobrenome, email, cpf):
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO cliente VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
        conn.commit()

def view():
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cliente")
        rows = cur.fetchall()
    return rows

def search(nome="", sobrenome="", email="", cpf=""):
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cliente WHERE nome=? OR sobrenome=? OR email=? OR cpf=?", (nome, sobrenome, email, cpf))
        rows = cur.fetchall()
    return rows

def delete(record_id):
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM cliente WHERE id=?", (record_id,))
        conn.commit()
        print(f"Deletado id: {record_id}")

def update(record_id, nome, sobrenome, email, cpf):
    with sqlite3.connect('clientes.db') as conn:
        cur = conn.cursor()
        cur.execute("UPDATE cliente SET nome=?, sobrenome=?, email=?, cpf=? WHERE id=?", (nome, sobrenome, email, cpf, record_id))
        conn.commit()

connect()
