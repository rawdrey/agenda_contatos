from data.banco import contatos


def contato_existe (nome):
    for c in contatos:
        if c ["nome"].lower == nome.lower:
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

def buscar_contatos(parte_nome):
    resultado = []
    for c in contatos:
        if parte_nome.lower() in c["nome"].lower():
            resultado.append (c)
    return resultado


def listar_contatos():
    return contatos


