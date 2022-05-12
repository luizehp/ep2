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
letra = 'letras da capital: '
dicas = ['DICAS: ']
cor = 'Cores da bandeira: '
restricao = []
ncor =[]
clr = True
cnt = True
letr = True
ara = True
pp = True
listp = []

print('\n\n ============================ ')
print('|                            |')
print('| Bem-vindo ao Insper países |')
print('|                            |')
print(' ==== Design de Softare ==== \n\n')
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
            for n in paises[r]['bandeira']:
              if paises[r]['bandeira'][n] > m and f'{n}' not in ncor:
                m = paises[r]['bandeira'][n]
                cr = n
        
            if cr == 'outras':
                clr = False

            print ('----------------------------------------')
            if clr == True:
                print ('1. Cor da bandeira  - custa 4 tentativas')
            if letr == True:
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

        
    
            if b == '1' and clr == True:
                m = 0
                for n in paises[r]['bandeira']:
                    if paises[r]['bandeira'][n] > m and f'{n}' not in ncor:
                        m = paises[r]['bandeira'][n]
                        cr = n
                ncor. append(cr)
                if f'{cor}' in dicas:
                    index = dicas. index(f'{cor}')
                    del dicas[index]
                cor += f'{cr},'
                i -= dica[0][2]  
                dicas.append(f'{cor}')
        
            elif b == '2' and letr == True:
                ltr = sorteia_letra(paises[r]['capital'], restricao)
                restricao. append (ltr)
                if f'{letra}' in dicas:
                    index = dicas. index(f'{letra}')
                    del dicas[index]
                letra += '{0},'. format(ltr)
                i -= dica[1][2]
                dicas.append(f'{letra}')
      
            
          
            elif b == '3' and ara == True:
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



    elif a in paises:
          d = haversine (EARTH_RADIUS, paises[r]['geo']['latitude'], paises[r]['geo']['longitude'], paises[a]['geo']['latitude'], paises[a]['geo']['longitude'])
          if l == []:
              l. append ([a, d])
          else:
              l = adiciona_em_ordem(a,d,l)
          i -= 1
          print('\n')
          for n in range (len(l)):
            x = int(l[n][1])
            x = ('{:,}'. format(x).replace(',','.'))
            if int(l[n][1]) >= 10000:
              print (f'{x} km -> {l[n][0]}')
            elif int(l[n][1]) >= 2000:
              print (f' {x} km -> {l[n][0]}')
            elif int(l[n][1]) >= 1000:
              print (f' {x} km -> {l[n][0]}')
            else:
              print (f'  {x} km -> {l[n][0]}')
          print (f'tentativas: {i}')


    elif a == 'inventario':
        print (f'tentativas: {i}')
        print('\n')
        for n in range (len(dicas)):
          print (dicas[n])
        print('\n')
        for n in range (len(l)):
            if int(l[n][1]) >= 10000:
                print (f'{x} km -> {l[n][0]}')
            elif int(l[n][1]) >= 2000:
                print (f' {x} km -> {l[n][0]}')
            elif int(l[n][1]) >= 1000:
                print (f' {x} km -> {l[n][0]}')
            else:
                print (f'  {x} km -> {l[n][0]}')

    else:
        print ('\npaís desconhecido')
        print (f'tentativas: {i}')
    


