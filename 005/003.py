

def media_matriz(matriz):
    """ Recebe uma matriz númerica. Com base no total
    da somatória de todos os elementos e as dimensões
    da matriz, calcula a média aritmética dos elementos
    da matriz
    
    list -> float """

    linhas = float(len(matriz))
    colunas = float(len(matriz[0]))
    total = 0
    for linha in matriz:
        for coluna in linha:
            total += float(coluna)
            
    media = (total / (linhas * colunas))
    return round(media,2)