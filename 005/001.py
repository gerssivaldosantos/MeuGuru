def eh_quadrada(matriz):
    """ Recebe uma matriz númerica e confere se suas
    dimensões constituem uma matriz quadrada
    list -> boolean """
    linhas = len(matriz)
    if matriz == []:
        colunas = 0
    else:
    	colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False