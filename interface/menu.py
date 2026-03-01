from services.contatos_service import(
    adcionar_contato,
    buscar_contatos,
    listar_contatos
)
from utils.validacoes import(
    validar_nome,
    validar_telefone,
    validar_email
)

def menu():
    while True:
        print("===Contatos Inteligente ===")
        print("1- Adcionar contato: ")
        print("2- Buscar contato: ")
        print("3- Listar contatos:  ")
        print("0- Sair: ")
        op = input("Escolha: ")
        try:
            if op == "1":
                nome = input("Nome: ")
                if not validar_nome(nome):
                    print("Nome inválido: ")
                    continue

                telefone = input("Telefone: ")
                if not validar_telefone (telefone):
                    print("Telefone inválido: ")
                    continue
                email = input("E-mail: ")
                if not validar_email (email):
                    print("E-mail inválido: ")
                    continue
                adcionar_contato (nome, telefone, email)
                print("Contato adcionado!")

            elif op == "2":
                busca = input("Digite parte do nome: ")
                resultado = buscar_contatos (busca)
                for c in resultado:
                    print(c)

            elif op == "3":
                for c in listar_contatos ():
                    print(c)
            elif op == "0":
                print("Encerrando: ")
                break
        except ValueError as erro:
            print(f"Erro: {erro}")
            