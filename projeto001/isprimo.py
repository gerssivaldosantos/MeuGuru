""" Faça uma função chamada primo que dado um número inteiro positivo,
 verifique se este número é primo ou não. Retorne um valor booleano. Dica: uma estratégia 
 simples para identificar a primalidade de um número é verificar se não existe nenhum número 
 menor que ele próprio (e maior ou igual a 2) que o divida.  Dica 2: O número de divisões indicado 
 na dica anterior é maior que o necessário. Você consegue reduzi-lo? """

def primo(numero):
    cont = 0
    for indice in range(2,numero):
        """ Percorrendo os intervalos entre 2 e o número anterior à entrada """
        if numero % indice == 0:
            """ Caso encontre números que dividem a entrada sem resto, retorna que
            False, caso não econtre, o retorno de fora do laço faz retorna Verdadeiro """
            return False
            break
            
    return True
        


print(primo(11))
