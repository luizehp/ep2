import random
import dados
DADOS = dados.DADOS


def sorteia_pais(lista):
    nlista = []
    for i in lista:
        nlista.append(i)
    return random.choice(nlista)