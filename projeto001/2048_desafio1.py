""" Escreva uma função que recebe uma lista numérica e some os números adjacentes
que sejam iguais, a soma deve ser feita da esquerda para a direita. A função deve
modificar a própria lista, retornando True se houve a modificação. """

def somar_adjacentes(numeros):
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
    if numeros != somados:
        numeros = somados
        return True
    else:
        return False

        
