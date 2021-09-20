""" Crie uma função que receba uma matriz numérica e substitua aleatoriamente um
dos números zeros da matriz pelos número 2 ou 4, onde o número 2 tem uma chance
maior de acontecer que o número 4. Se a inserção não puder ser feita, deve retorna
False, caso contrário True.
Dica: olhe a função random.choices """

from random import choice

def substituir_matriz(matriz):
    #extraindo o tamanho da matriz para percorre-la
    len_lin = len(matriz)
    len_col = len(matriz[0])
    #extraindo as posicoes dos numeros zeros
    zeros_posi = []
    for linha in range(len_lin):
        for coluna in range(len_col):
            if matriz[linha][coluna] == 0:
                zeros_posi.append((linha,coluna))

    #Escolhendo qual dos zeros substituir 
    zero_sorteado = choice(zeros_posi)
    
    #Fazendo com que o 2 seja mais provavel de ser 
    #escolhido como substituto
    substitutos = (2,2,4)
    substituto = choice(substitutos)

    #Substituindo
    matriz[zero_sorteado[0]][zero_sorteado[1]] = substituto

    return matriz


