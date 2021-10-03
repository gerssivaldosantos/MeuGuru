""" Crie uma função para mostrar o tabuleiro de 2048.
Cuidado!!! Ao começarem a aparecer números maiores o tabuleiro mostrado
não pode deixar o formato padrão Para o jogo não ficar poluı́do substitua 
zeros por ’*’ ou ’-’ quando for
mostrar para o jogador """



def montar_tabuleiro(matriz):
    """ Monta um tabuleiro de 2048 a partir de 
    uma matriz."""
    #dimensões da matriz
    len_linha = len(matriz)
    len_coluna = len(matriz[0])

    print("-"* len_coluna * 16)

    for linha in range(len_linha):
        for coluna in range(len_coluna):
            if matriz[linha][coluna] != 0:
                elemento = f"|{matriz[linha][coluna]:^15}"
            else:
                elemento = f"|{'-':^15}"
            print(elemento,end="")
            
        print("|")
        print("-"* len_coluna * 16)

montar_tabuleiro(
    [[2,3,4,19310,342],
     [2,3,4,34,2],
     [4,5,0,4,3]]
)

