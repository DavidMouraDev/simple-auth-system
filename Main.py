import hashlib
import sqlite3

login = int(input('Deseja logar(1) ou criar uma conta(2)? '))

conexao = sqlite3.connect('Users.db')
cursor = conexao.cursor()

sql_cria_tabela = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL
)
"""

cursor.execute(sql_cria_tabela)
conexao.commit()

if login == 1:
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()


    sql = "SELECT id, email, senha_hash FROM users WHERE email = ?"
    cursor.execute(sql, (email,))

    usuario = cursor.fetchone()

    if usuario is None:
        print('E-mail não encontrado!')
    else:
        id_usuario, email_banco, hash_salvo = usuario

        if senha_hash == hash_salvo:
            print(f'Login realizado com sucesso! Bem-vindo!')
        else:
            print('Senha incorreta!')

elif login == 2:
    email = input('Digite seu email para a criação da conta: ')
    senha = input('Crie uma senha: ')

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    sql = "INSERT INTO users (email, senha_hash) VALUES (?, ?)"

    try:
        cursor.execute(sql, (email, senha_hash))
        conexao.commit()
        print("Usuário cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Este e-mail já está cadastrado no sistema!")

conexao.close()