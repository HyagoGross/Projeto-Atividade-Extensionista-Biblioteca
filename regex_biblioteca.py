import re
def validatelefone(telefone):
    target=telefone
    pattern=re.compile("^\(?[0-9]{0,2}\)?[\s\S]?[0-9]{5}[\-]?[0-9]{4}$")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validacpf(cpf):
    target=cpf
    pattern=re.compile("^[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}$")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validamat(matricula):
    target=matricula
    pattern=re.compile("[0-9]*")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validaid(id):
    target=id
    pattern=re.compile("^[0-9A-z]{1,5}$")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validanome(nome):
    target=nome
    pattern=re.compile("[A-zÁ-úÂ-ôÃ-õ]+[\s\S]*")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validacategoriaLivro(categoria):
    target=categoria
    pattern=re.compile("[A-zÁ-úÂ-ôÃ-õ]+[\s\S]*")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False
def validadata(data):
    target=data
    pattern=re.compile("[0-9]{1,2}[/-][0-9]{1,2}[/-][0-9]{4}")
    match= re.fullmatch(pattern,target)
    if(match!=None):
        return True
    else:
        return False