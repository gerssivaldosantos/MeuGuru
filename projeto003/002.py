def conta_numero(numero,matriz):
    """ Recebe um número e uma matriz númerica,
    procura na matriz por esse número dado como 
    entrada e retorna o a quantidade de vezes em 
    que ele ocorre
    
    int, list -> int
     """
    num_vezes = 0
    
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                num_vezes += 1
    return num_vezes