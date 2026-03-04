from services.contatos_service import (
    adcionar_contato,
    buscar_contatos,
    listar_contatos
)

from utils.validacoes import (
    validar_nome,
    validar_telefone,
    validar_email
)

from interface.formatacao import mostrar_contato


def menu():
    while True:
        print("=== Contatos Inteligente ===")
        print("1- Adcionar contato")
        print("2- Buscar contato")
        print("3- Listar contatos")
        print("0- Sair")

        op = input("Escolha: ")

        try:
            if op == "1":
                nome = input("Nome: ")
                if not validar_nome(nome):
                    print("Nome inválido")
                    continue

                telefone = input("Telefone: ")
                if not validar_telefone(telefone):
                    print("Telefone inválido")
                    continue

                email = input("E-mail: ")
                if not validar_email(email):
                    print("E-mail inválido")
                    continue

                adcionar_contato(nome, telefone, email)
                print("Contato adicionado!")

            elif op == "2":
                busca = input("Digite parte do nome: ")
                resultado = buscar_contatos(busca)

                if not resultado:
                    print("Nenhum contato encontrado.")
                else:
                    for c in resultado:
                        mostrar_contato(c)

            elif op == "3":
                lista = listar_contatos()

                if not lista:
                    print("Nenhum contato cadastrado.")
                else:
                    for c in lista:
                        mostrar_contato(c)

            elif op == "0":
                print("Encerrando...")
                break

            else:
                print("Opção inválida.")

        except ValueError as erro:
            print(f"Erro: {erro}")