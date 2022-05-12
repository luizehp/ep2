import random 
import math
EARTH_RADIUS = 6371
import dados
DADOS = dados.DADOS



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
    return 2 * r * (math.asin((((math.sin((math.radians((a-x)/2))))*2) + ((math.cos(math.radians(x))*math.cos(math.radians(a))) * ((math.sin((math.radians((b-y)/2))))2)))*(1/2)))

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

continuar = 0
paises = normaliza (DADOS)
print('=====================================================================================================================================================')
x = []
for i in paises:
    x. append (i)
r = random. choice(x)
i = 20
l = []
a = 0
dicas = ['DICAS: ']
cnt = True
ara = True
pp = True
listp = []

print(f'\n\n============================ ')
print('|                            |')
print('| Bem-vindo ao Insper países |')
print('|                            |')
print(f' ==== Design de Softare ==== \n\n')
print(' Comandos:')
print('     dica       - entra no mercado de dica')
print('     desisto    - desiste da rodada')
print('     inventario - exibe sua posição')


while i > 0:
    print ('----------------------------------------------------------------------------------------------------------------------------')
    print('\n')
    a = input ('país: ')
    a = a.lower()
    while a in listp:
        print ('\nVocê ja tentou este país\n')
        a = input ('\npaís: ')
        listp. append (a)
        if a == r:
            print ('GANHOU!')
            break
    if a == 'dica':
            print('\n')
            dica = [[1, 'Cores da bandeira do país', 4], [2, 'Letras de sua capital',3], [3, 'Área',6], [4, 'População',5], [5, 'Continente',7], [0,'sem dica',0]]
            m = 0
            print ('----------------------------------------')
            print ('1. Cor da bandeira  - custa 4 tentativas')
            print ('2. Letra da capital - custa 3 tentativas')
            if ara == True:
                print ('3. Área             - custa 6 tentativas')
            if pp == True:
                print ('4. População        - custa 5 tentativas')
            if cnt == True:
                print ('5. Continente       - custa 7 tentativas')
            print ('0. Sem dica')
            print ('----------------------------------------')


            b = input('\nescolha opção [0|1|2|3|4|5]: ')
            d = b.lower()
      
            
          
            if b == '3' and ara == True:
                area = paises[r]['area']
                ar = f'Área: {area}' 
                dicas.append(ar)
                i -= dica[2][2]
                ara = False
              

            elif b == '4' and pp == True:
                pop = paises[r]['populacao']
                dicas.append(f'População: {pop}')
                i -= dica[3][2]
                pp = False
            

            elif b == '5' and cnt == True:
                pop = paises[r]['continente']
                dicas.append(f'Continente: {pop}')
                i -= dica[4][2]
                cnt = False
              
          
            else:
                print('opção inválida')
            print(f'{dicas[0]}')
            for n in range (1,len(dicas)):
                print (f'    {dicas[n]}')
        
            if i < dica[1][2]:
                letr = False
            if i < dica[0][2]:
                clr = False
            print (f'tentativas:{i}')