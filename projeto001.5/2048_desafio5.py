""" Faça uma função que receba duas matrizes e confere se elas são iguais, retornando
True caso seja verdade False caso não seja """

def comparar_matrizes(matriz1, matriz2):
    len_lin1 = len(matriz1)
    len_lin2 = len(matriz2)
    len_col1 = len(matriz1[0])
    len_col2 = len(matriz2[0])
    if len_lin1 == len_lin2 and len_col1 == len_col2:
        for linha in range(len_lin1):
            for coluna in range(len_col1):
                if matriz1[linha][coluna] != matriz2[linha][coluna]:
                    return False
                else:
                    pass
    else:
        return False
        
    return True

print(comparar_matrizes(
    [[0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0]], 

[
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 3, 0, 0], 
     [0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0]]))
