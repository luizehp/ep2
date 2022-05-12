import math
EARTH_RADIUS = 6371
import dados
DADOS = dados.DADOS
import random 



def normaliza (a):
    d = {}
    for i in a:
        for n in a[i]:
            d[n] = a[i][n]
            d [n]['continente'] = i
    return d

def sorteia_pais(lista):
    nlista = []
    for i in lista:
        nlista.append(i)
    return random.choice(nlista)

def haversine(r,x,y,a,b):
    return 2 * r * (math.asin((((math.sin((math.radians((a-x)/2))))**2) + ((math.cos(math.radians(x))*math.cos(math.radians(a))) * ((math.sin((math.radians((b-y)/2))))**2)))**(1/2)))

def adiciona_em_ordem(a,b,l):
    n=0
    for i in range (0, len (l)):
        if l[i][1] < b:
            n = i + 1
    l. insert (n, [a,b])
    return l


def esta_na_lista(pais, lista):
    for i in lista:
        if i[0] == pais:
            return True
    return False

def sorteia_letra(y,b):
    l = []
    k = ['.', ',', '-', ';', ' ']
    a = y. lower()
    for i in range(len(a)):
        l. append (a[i])
    x = random. choice(l)
    z = True
    for i in a:
        if i not in b and i not in k:
            z = False
    if z == True:
        return ''
    while x in b or x in k:
        x = random. choice(l)
    return x
