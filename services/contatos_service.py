from data.banco import contatos
from data.arquivo import salvar_contato


def contato_existe (nome):
    nome = nome.strip().lower()
    for c in contatos:
        if c["nome"].strip().lower() == nome:
            return True
    return False


def adcionar_contato(nome,telefone,email):
    if contato_existe (nome):
        raise ValueError ("Contato já cadastrado")
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }
    contatos.append (contato)
    salvar_contato (contato)


def buscar_contatos(parte_nome):
    resultado = []
    for c in contatos:
        if parte_nome.lower() in c["nome"].lower():
            resultado.append (c)
    return resultado


def listar_contatos():
    return contatos


