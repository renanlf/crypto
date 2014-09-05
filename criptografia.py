#-------------------------------------------------------------------------------
# Author:      Renan Leandro
#-------------------------------------------------------------------------------

from random import randint

#MÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo utilizado para fator um nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero. Insere o nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero e tem como resultado uma lista
#com os nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmeros que o formam!
def fatoracao(numero):
    fatores = []
    fator = 2
    numero = int(numero)
    while fator <= numero:
        if numero % fator == 0:
            fatores.append(fator)
            numero = numero/fator
        else:
            fator = fator + 1
    return fatores

#Este mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo recebe o valor a, e o n, que ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© o tamanho do conjunto Z(dos restos) que
# vocÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âª estÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ trabalhando, trazendo assim o seu inverso.
def inverso(a, b):
    a = int(a)
    b = int(b)

    i = 1

    while i < b and (a*i)%b != 1: #(a*i) mod p diferente de 1
        i = i + 1;

    return i;

#Este mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo traz as duas raÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­zes de um nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero, dado o nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero p.
#Obs o p deve ser congruente a 3(mod4)!
def raiz(numero, p):
    resultado = []
    numero = int(numero)
    if (p - 4) % 3 != 0:
        return []
    s = (p+1)/4
    s = int(s)
    raiz = (numero**s) % p

    resultado.append(raiz)
    raiz = p - raiz
    resultado.append(raiz)
    return resultado

#Este mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo traz todas as 4 raÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­zes de um nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero dados p e q.
#ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¨ bastante ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºtil pois resume em um sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â³ mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo as 2 raÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­zes de p e as duas de q!
def raizes(numero, p, q):
    raiz1 = raiz(numero, p)
    raiz2 = raiz(numero, q)

    resultado = []
    resultado.append(raiz1[0])
    resultado.append(raiz1[1])
    resultado.append(raiz2[0])
    resultado.append(raiz2[1])

    return resultado

#Este mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© baseado no Teorema do Resto ChinÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âªs.
#Dados os restos e seus mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â³dulos ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© possÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­vel calcular um outro resto em relaÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â§ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â£o a mod1*mod2
def restoChines(resto1, mod1, resto2, mod2):
    resto1 = int(resto1)
    mod1 = int(mod1)
    resto2 = int(resto2)
    mod2 = int(mod2)

    sub = resto2 - resto1
    if sub < 0:
        sub = sub + mod2

    resultado = (sub*inverso(mod1, mod2)) % mod2

    return (resultado*mod1) + resto1

#Aqui ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© onde ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© obtido o e utilizado como expoente em RSA.
#Obs.: utiliza o randint para pegar um nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero aleatÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â³rio de 1 atÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© o nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero phi
def ePhi(p, q):
    p = int(p)
    q = int(q)
    phi = (p-1) * (q-1)
    return(randint(1,phi))

def criptografarRabin(mensagem, n):
    mensagem = int(mensagem)
    n = int(n)
    N = (mensagem**2) % n
    return N

#Utilizando o resto chinÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âªs, este mÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â©todo traz as quatro possÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â­veis mensagens originais.
def descriptografarRabin(mensagem, p, q):
    lista = raizes(mensagem, p, q)

    resultado = []
    resultado.append(restoChines(lista[0], p, lista[2], q))
    resultado.append(restoChines(lista[0], p, lista[3], q))
    resultado.append(restoChines(lista[1], p, lista[3], q))
    resultado.append(restoChines(lista[1], p, lista[2], q))

    return resultado

# Esta chave pÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºblica ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© que serÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ enviada para a pessoa que deseja enviar a mensagem, estÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ organizada na forma: [n, e]
# n ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© o nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmero obtido por p*q e e ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© o expoente utilizado para criptografar!
def chavePublicaRSA(p, q):
    resultado = []
    e = ePhi(p, q)
    n = p*q

    resultado.append(n)
    resultado.append(e)

    return resultado

#Ao receber a chave pÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºblica quem deseja enviar a mensagem a converte para ASCII ou outro padrÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â£o e com isso tem o M
# Insere o M, e e n e terÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ a mensagem criptograda, podendo enviar ela ao receptor
def criptografarRSA(M, e, n):
    N = (M**e) % n
    return N

#Como o receptor jÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â¡ sabe quem sÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â£o os nÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Âºmeros que formam n(p e q) e sabe quem ÃƒÆ’Ã†â€™Ãƒâ€šÃ‚Â© o inverso de e em Z de (p-1)*(q-1), ou seja d
# Pode descriptografar sem problema inserindo a mensagem recebida N, e, p e q, obtendo assim a mensagem original M!
def descriptografarRSA(N, e, p, q):
    d = inverso(e, (p-1)*(q-1))
    M = (N**d) % (p*q)
    return M


#####################Testando ########################


#print(fatoracao(328419349))

#print(restoChines(2793, 7243, 21983, 45343))

#print(descriptografarRabin(484, 19, 31))

#print(descriptografarRSA(322776966, 220037467, 45343, 7243)) # pigs

#print(descriptografarRSA(18035306, 220037467, 45343, 7243)) # pigs

#print(inverso(19, 31))

N = criptografarRabin(10301, 589)

a = N % 19
b = N % 31

c = raiz(a, 19)
d = raiz(b, 31)

M = descriptografarRabin(N, 19, 31)

