import os
import re
import json
from time import sleep as sp
from passlib.context import CryptContext

# Configuração do passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para limpar a tela
def clear():
    os.system('cls')  # Limpa a tela no Windows
    # Para Linux ou MacOS, use: os.system('clear')


# Função para validar o e-mail
def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))


# Função para criptografar senha
def criptografar_senha(senha):
    return pwd_context.hash(senha)


# Função para verificar se a senha está correta
def verificar_senha(senha_informada, senha_armazenada):
    return pwd_context.verify(senha_informada, senha_armazenada)


# Função para salvar dados do usuário
def salvar_dados(usuario_nome, usuario_email, senha_criptografada):
    dados = {
        'nome': usuario_nome,
        'email': usuario_email,
        'senha': senha_criptografada
    }
    with open('usuario.json', 'w') as f:
        json.dump(dados, f)


# Função para carregar dados do usuário
def carregar_dados():
    if os.path.exists('usuario.json'):
        with open('usuario.json', 'r') as f:
            return json.load(f)
    return None


# Função para gerenciar o usuário
def gerenciar_usuario():
    clear()
    print("\033[1;32m => [Gerenciando usuario...]" + "\033[0m")
    sp(2)

    senha_informada = input("\033[1;32mDigite a senha do usuario: \033[0m")

    # Verifica se a senha informada é a correta
    if verificar_senha(senha_informada, senha_armazenada):
        print(f"\033[1;33m\n[::] Nome: \033[0m{usuario_nome}")
        print(f"\033[1;33m[::] Email: \033[0m{usuario_email}")
        print(f"\033[1;33m[::] Senha: \033[0m(Protegida)")
    else:
        print("\033[1;31mSenha incorreta.\033[0m")

    print()
    voltar = input("\033[1;34m(Digite [99] para voltar): \033[0m")

    if voltar == "99":
        return  # Volta para o menu principal


# Função para criar ou recuperar uma conta
def criar_ou_recuperar_conta():
    dados_usuario = carregar_dados()
    print("\n\t\033[1;34m" + """
+____________________+
|                    |
|  BNEC - Ferramenta |
|____________________|
""" + "\033[0m")
    if dados_usuario:
        print("\033[1;34m[::] Conta já existente.\033[0m")
        print("""\033[1;34m
[1]  Entrar 
[2]  Criar conta
\033[0m""")
        escolha = input("\033[1;32m[@]: \033[0m")
        
        if escolha == '1':
            senha_informada = input("\033[1;32mDigite a senha para login: \033[0m")

            if verificar_senha(senha_informada, dados_usuario['senha']):
                print("\033[1;32mLogin bem-sucedido!\033[0m")
                return dados_usuario  # Retorna os dados carregados
            else:
                print("\033[1;31mSenha incorreta.\033[0m")
                return None
        elif escolha == '2':
            print("\033[1;34m[::] Criando uma nova conta...\033[0m")
            return criar_nova_conta()
        else:
            print("\033[1;31mOpção inválida.\033[0m")
            return None
    else:
        print("\033[1;34m[::] Bem-vinda (o)!...\033[0m")
        return criar_nova_conta()


# Função para criar uma nova conta
def criar_nova_conta():
    usuario_nome = input("\033[1;32mDigite o nome do usuario: \033[0m")
    usuario_email = input("\033[1;32mDigite o e-mail do usuario: \033[0m")

    while not validar_email(usuario_email):
        print("\033[1;31mEmail inválido. Tente novamente.\033[0m")
        usuario_email = input("\033[1;32mDigite o e-mail do usuario: \033[0m")

    senha = input("\033[1;32mDigite a senha do usuario: \033[0m")
    senha_criptografada = criptografar_senha(senha)
    
    salvar_dados(usuario_nome, usuario_email, senha_criptografada)
    print("\033[1;32mConta criada com sucesso!\033[0m")
    return {'nome': usuario_nome, 'email': usuario_email, 'senha': senha_criptografada}


# Função principal
def bne():
    usuario = criar_ou_recuperar_conta()
    print("\n\t\033[1;34m" + """
+____________________+
|                    |
|  BNEC - Ferramenta |
|____________________|
""" + "\033[0m")
    if usuario:
        while True:
            comando = input("\033[1;34mBNEC> \033[0m")
            if comando == "usuario":
                gerenciar_usuario()
            elif comando == "sair":
                print("\033[1;31mSaindo da ferramenta...\033[0m")
                break
            else:
                print("\033[1;31mComando inválido!\033[0m")


bne()
