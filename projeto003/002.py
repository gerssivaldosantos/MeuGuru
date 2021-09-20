def conta_numero(numero,matriz):
    num_vezes = 0
    
    for linha in matriz:
        for coluna in linha:
            if coluna == numero:
                num_vezes += 1
    return num_vezes