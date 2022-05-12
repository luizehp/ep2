import random
import dados
DADOS = dados.DADOS


def sorteia_pais(lista):
    nlista = []
    for i in lista:
        nlista.append(i)
    return random.choice(nlista)

def esta_na_lista(pais, lista):
    for i in lista:
        if i[0] == pais:
            return True
    return False