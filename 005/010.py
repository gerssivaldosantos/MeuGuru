""" Crie uma função que pega um número do usuário, confira se é uma potência de 2, e
então retorne o número inteiro. Por exemplo, se o usuário digitar 64, é um número
válido, já se digitar 78, não é um número plausı́vel. Atenção: Lembre-se que o
usuário pode digitar qualquer coisa no shell não somente números
Atenção 2: A função recebe a informação a partir no shell, não confunda
com parâmetros """

def potencia_de_2():
    """ Lê um número e retorna a entrada caso
    ela seja potência de 2, caso não seja, não
    faz retorno

    str -> int
     """
    permanecer = True

    #Laço infinito para prender o usuário caso não
    #digite a informação que se pede

    while permanecer:
        #O laço funciona com a saída explicita
        #e a permanencia implicita na condicional
        #que é disparada ao achar um caracter inválido
        permanecer = False
        errado = False
        numero = str(input("Digite um número inteiro : "))
        #Caracteres esperados na entrada do usuario
        numeros = ["0","1","2","3","4","5","6","7","8","9"]

        #Conferindo entrada vazia
        if len(numero) != 0:

            #Conferindo número negativo
            if numero[0] == "-":
                if len(numero) > 1:                
                    for index in range(1,len(numero)):
                        if numero[index] not in numeros:
                            errado = True                           
                else:
                    errado = True                  
            else:
                #Conferindo números positivos
                for num in numero:
                    if num not in numeros:
                        errado = True
        else:
            errado = True
        if errado:
            permanecer = True 
            print("Entrada inválida. ",end="") 

    #Convertendo a entrada para inteiro 
    #Conferindo se a entrada é potencia de 2

    numero = int(numero)
    dividido = numero
    
    while True:
        resto = dividido % 2
        dividido = dividido / 2
        if dividido == 1:
            return numero
        elif resto > 0:
            break
                    
                
