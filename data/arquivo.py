import os
from data.banco import contatos

caminho_arquivo = "data/contatos.csv"


def carregar_contatos():
    if not os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "w", encoding="utf-8-sig") as f:
            f.write("nome;telefone;email\n")
        return

    with open(caminho_arquivo, "r", encoding="utf-8-sig") as f:
        linhas = f.readlines()

    for linha in linhas[1:]:
        linha = linha.strip()
        if not linha:
            continue

        nome, telefone, email = linha.split(";")

        contato = {
            "nome": nome.strip(),
            "telefone": telefone.strip(),
            "email": email.strip()
        }

        contatos.append(contato)


def salvar_contato(contato):
    with open(caminho_arquivo, "a", encoding="utf-8-sig") as f:
        linha = f'{contato["nome"]};{contato["telefone"]};{contato["email"]}\n'
        f.write(linha)