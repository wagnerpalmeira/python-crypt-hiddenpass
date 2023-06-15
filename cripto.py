import bcrypt
import sqlite3
import getpass


conn = sqlite3.connect('aula_database') 
c = conn.cursor()

def cadastrar_usuario(conexao, nome, senha):
    cursor = conexao.cursor()
    senha = criotpgrafar(senha)
    sql = f'INSERT INTO usuarios(name, senha) VALUES (?, ?)'
    cursor.execute(sql, [nome, senha])
    conexao.commit()
    
    return True


def autenticar(conexao, usuario):
    cursor = conexao.cursor()
    sql = 'select * from usuarios WHERE name=?'
    cursor.execute(sql, [
        usuario
    ])
    
    return cursor.fetchall()


def criotpgrafar(password):
    bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed

def checar_password(password, hashed):
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed)

while True:
    opcao = int(input("Digite opcao: "))
    
    # Cadastrar
    if opcao==1:
        nome = input("Digite o novo usuário: ")
        senha = getpass.getpass('Password:')
        cadastrar_usuario(conn, nome, senha)
    # Autenticar
    elif opcao == 2:
        usuario = input("Digite usuario: ")
        senha = getpass.getpass('Password:')
        usuario_autenticado = autenticar(conn, 
                                            usuario)
        
        if len(usuario_autenticado) > 0 and checar_password(senha, usuario_autenticado[0][2]):
            print("Logado")
        else:
            print("Login e senha inválidos.")