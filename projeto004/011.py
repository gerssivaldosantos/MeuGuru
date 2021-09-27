""" Crie uma função que irá pegar alguma jogada válida do usuário. No 2048, as
jogadas válidas serão ’a’, ’s’, ’d’, ’w’. Não aceite qualquer outro tipo de informação
Atenção 2: A função recebe a informação a partir no shell, não confunda
com parâmetros """

def receber_jogada():

    """ Lê uma jogada e confere se ela é válida """

    #Lista com as jogadas válidas
    validas = ["a","s","d","w"]
    while True:
        #Conferindo se a jogada faz parte do conjunto
        #de válidas
        jogada = str(input("Digite a jogada :"))
        if jogada in validas:
            break
        else:
            print("Jogada inválida. ",end="")
