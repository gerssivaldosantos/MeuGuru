def eh_quadrada(matriz):
    linhas = len(matriz)
    if matriz == []:
        colunas = 0
    else:
    	colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False