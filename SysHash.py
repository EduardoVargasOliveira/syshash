import bcrypt
users_db = {}  
def register_user():
    username = str(input("Crie um nome de usuario: "))
    if username in users_db:
        print("Usuario ja existe!")
        return
    pw = str(input("Crie uma senha: "))
    pw_bytes = pw.encode('utf-8')
    hashed = bcrypt.hashpw(pw_bytes, bcrypt.gensalt())
    users_db[username] = hashed
    print("Nome de usuario e senha salvos com sucesso!")
def login_user():
    username = str(input("Digite o nome de usuario: "))
    if username not in users_db:
        print("Usuario nao encontrado!")
        return
    else:
        pw = str(input("Digite a senha: "))
        pw_bytes = pw.encode('utf-8')
        if bcrypt.checkpw(pw_bytes, users_db[username]):
            print(f"Bem-vindo, {username}!")
        else:
            print("Senha invalida!")
            return

while True:
    resp = str(input("Voce quer [C]riar-usuario [E]ntrar-usuario [S]air: "))
    if resp in "Cc":
        register_user()
    elif resp in "Ee":
        login_user()
    elif resp in "Ss":
        break
    else:
        print("Opcao invalida.")
exit
