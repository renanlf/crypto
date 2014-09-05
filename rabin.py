#-------------------------------------------------------------------------------
# Author:      Renan Leandro
#-------------------------------------------------------------------------------

from random import randint

#Método utilizado para fator um número. Insere o número e tem como resultado uma lista
#com os números que o formam!
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

#Este método recebe o valor a, e o n, que é o tamanho do conjunto Z(dos restos) que
# você está trabalhando, trazendo assim o seu inverso.
def inverso(a, b):
    a = int(a)
    b = int(b)

    i = 1

    while i < b and (a*i)%b != 1: #(a*i) mod p diferente de 1
        i = i + 1;

    return i;

#Este método traz as duas raízes de um número, dado o número p.
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

#Este método traz todas as 4 raízes de um número dados p e q.
#è bastante útil pois resume em um só método as 2 raízes de p e as duas de q!
def raizes(numero, p, q):
    raiz1 = raiz(numero, p)
    raiz2 = raiz(numero, q)

    resultado = []
    resultado.append(raiz1[0])
    resultado.append(raiz1[1])
    resultado.append(raiz2[0])
    resultado.append(raiz2[1])

    return resultado

#Este método é baseado no Teorema do Resto Chinês.
#Dados os restos e seus módulos é possível calcular um outro resto em relação a mod1*mod2
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

#Aqui é onde é obtido o e utilizado como expoente em RSA.
#Obs.: utiliza o randint para pegar um número aleatório de 1 até o número phi
def ePhi(p, q):
    p = int(p)
    q = int(q)
    phi = (p-1) * (q-1)
    return(randint(1,phi))

def criptografarRabin(mensagem, n):
    return 0


#Utilizando o resto chinês, este método traz as quatro possíveis mensagens originais.
def descriptografarRabin(mensagem, p, q):
    lista = raizes(mensagem, p, q)

    resultado = []
    resultado.append(restoChines(lista[0], p, lista[2], q))
    resultado.append(restoChines(lista[0], p, lista[3], q))
    resultado.append(restoChines(lista[1], p, lista[3], q))
    resultado.append(restoChines(lista[1], p, lista[2], q))

    return resultado

# Esta chave pública é que será enviada para a pessoa que deseja enviar a mensagem, está organizada na forma: [n, e]
# n é o número obtido por p*q e e é o expoente utilizado para criptografar!
def chavePublicaRSA(p, q):
    resultado = []
    e = ePhi(p, q)
    n = p*q

    resultado.append(n)
    resultado.append(e)

    return resultado

#Ao receber a chave pública quem deseja enviar a mensagem a converte para ASCII ou outro padrão e com isso tem o M
# Insere o M, e e n e terá a mensagem criptograda, podendo enviar ela ao receptor
def criptografarRSA(M, e, n):
    N = (M**e) % n
    return N

#Como o receptor já sabe quem são os números que formam n(p e q) e sabe quem é o inverso de e em Z de (p-1)*(q-1), ou seja d
# Pode descriptografar sem problema inserindo a mensagem recebida N, e, p e q, obtendo assim a mensagem original M!
def descriptografarRSA(N, e, p, q):
    d = inverso(e, (p-1)*(q-1))
    M = (N**d) % (p*q)
    return M


#####################Testando ########################


#print(fatoracao(328419349))

#print(restoChines(2793, 7243, 21983, 45343))

#print(descriptografarRabin(232732214, 7243, 45343))






