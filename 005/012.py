""" Crie a função que movimentará o tabuleiro para direita, esquerda, cima e baixo.
Pode ser uma função única que recebe como parâmetro o tabuleiro e a movimentação 
ou várias funções que recebem só o tabuleiro. Essas funções devem
movimentar o tabuleiro na mesma posição, ou seja, elas não retornarão nada.
Dica: Para a movimentação em cima e baixo, utilize a função transposta já feita """

from random import randint
from random import choice

def receber_jogada():
    """ Lê uma jogada e confere se ela é válida """
    #Lista com as jogadas válidas
    validas = ["a","s","d","w"]
    while True:
        #Conferindo se a jogada faz parte do conjunto
        #de válidas
        jogada = str(input("Digite a jogada : "))
        if jogada.lower() in validas:
            return jogada.lower()

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

def gerar_aleatorio(matriz):
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

def criar_tabuleiro(n = 4):
    matriz = []
    while True:
        #Sorteando as posições onde será preenchido
        posicao1 = [randint(0,n - 1),randint(0,n - 1)]
        posicao2 = [randint(0,n - 1),randint(0,n - 1)]
        #Garantindo que as posições sorteadas não sejam iguais
        if posicao1 != posicao2:
            break
    
    #percorrendo a matriz e alocando os números nas posições 
    #sorteadas
    for linhas in range(n):
        linha = []
        for colunas in range(n):
            if [linhas,colunas] == posicao1 or [linhas,colunas] == posicao2:
               
                linha.append(2)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def transpor_matriz(matriz):
    #extraindo tamanho da matriz
    len_lin = len(matriz)
    len_col = len(matriz[0])
    matriz_transposta = []

    #Criando uma matriz auxiliar
    #com as dimensões da transposta 
    for linha in range(len_col):
        nova_linha = []
        for coluna in range(len_lin):
            nova_linha.append(None)
        matriz_transposta.append(nova_linha)
    
    #Percorrendo a matriz original e alocando 
    #Os dados na transposta
    for linha in range(len_lin):
        for coluna in range(len_col):
            matriz_transposta[coluna][linha] = matriz[linha][coluna]

    return matriz_transposta

def somar_adjacentes(numeros, direcao):
    if direcao == "d":
        index_excluidos = []
        tamanho = len(numeros)
        somados = []
        for i in range(0,tamanho - 1):
            numero_atual = numeros[i]
            numero_proximo = numeros[i + 1]
            index_atual = i 
            index_proximo = i + 1
            if index_atual not in index_excluidos:
                if numero_atual == numero_proximo:
                    soma = numero_atual + numero_proximo
                    index_excluidos.append(index_proximo)
                    somados.append(0)
                    somados.append(soma)
                else:
                    somados.append(numero_atual)
                    
        if numeros[tamanho - 1] != numeros[tamanho - 2]:
            somados.append(numeros[tamanho -1])

        if somados != numeros:
            print("Mesmo resultado")
            return somados
        else:
            return somados

    elif direcao == "a":
        #INVERSÃO DA LISTA NUMERICA PASSADA COMO PARAMÊTRO
        original = numeros
        numeros = []
        for i_numeros in range(len(original)-1,-1,-1):
            numeros.append(original[i_numeros])

        index_excluidos = []
        tamanho = len(numeros)
        somados = []
        for i in range(0,tamanho - 1):
            numero_atual = numeros[i]
            numero_proximo = numeros[i + 1]
            index_atual = i 
            index_proximo = i + 1
            if index_atual not in index_excluidos:
                if numero_atual == numero_proximo:
                    soma = numero_atual + numero_proximo
                    index_excluidos.append(index_proximo)
                    somados.append(0)
                    somados.append(soma)
                else:
                    somados.append(numero_atual)
                    
        if numeros[tamanho - 1] != numeros[tamanho - 2]:
            somados.append(numeros[tamanho -1])

        #DESINVERSÃO DA LISTA PASSADA COMO PARAMETRO
        numeros = original

        #INVERSÃO DA SAIDA
        soma_original = somados
        somados = []
        for index in range(len(soma_original) - 1, -1, -1):
            somados.append(soma_original[index])

        if somados == numeros:
            print("Mesmo resultado")
            return somados
        else:
            return somados

def mover_posicao(matriz, direcao):
    copia = []
    len_linha = len(matriz)
    len_coluna = len(matriz[0])
    montar_tabuleiro(matriz)
 
    if direcao == "d":
        while True:
            for l in matriz:
                linha = []
                for c in l:
                    linha.append(c)
                copia.append(linha)

            

            if direcao == "d":
                for linha in range(len_linha):
                    for coluna in range(len_coluna - 1):
                        atual = matriz[linha][coluna]
                        prox = matriz[linha][coluna + 1]
                        if atual != 0 and prox == 0:
                            copia[linha][coluna + 1] = atual
                            copia[linha][coluna] = 0                                 
            if matriz == copia:
                break

            matriz = copia
            copia = []
    
    


    

            
    
mover_posicao([[1,0,1],[1,1,0],[0,1,0]],"d")
            


def mover_tabuleiro(tabuleiro):
    """ Recebe uma jogada do usuario e
     move o tabuleiro de acordo com as regras do 
    jogo 2048 e retorna o tabuleiro movido
    
    list -> list """
    """ Funcionamento base da função:
            É usada a "somar_adjacentes" nas linhas
            do tabuleiro dado como entrada caso as
            jogadas sejam horizontais, se forem na
            vertical, uso a função "transpor_matriz"
            e faço a mesma coisa. """
    jogada = receber_jogada()
    aux = list()
    if jogada == "d":
        for linha in tabuleiro:
            aux.append(somar_adjacentes(linha,jogada))
    montar_tabuleiro(tabuleiro)
    if tabuleiro == aux:
        print("igual")
    montar_tabuleiro(aux)

        

#mover_tabuleiro(criar_tabuleiro())