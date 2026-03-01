def validar_nome(nome):
    return len(nome.strip())>=5           


def validar_telefone(telefone):   
    return telefone.isdigit()

def validar_email(email):
    return"@" in email and "." in email
