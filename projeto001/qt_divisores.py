def qtd_divisores(numero):
    contador = 0
    """ Percorrendo do 1 ao número e verificando se o resto de divisão de cada
    número no intervalo é igual à zero, caso seja, adição ao contador """
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
            contador += 1
    return contador

