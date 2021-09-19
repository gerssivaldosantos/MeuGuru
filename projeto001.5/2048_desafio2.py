""" 
(2) Modifique ligeiramente a função 1, para receber dois parâmetros, a lista e a direção
(esquerda/direita) para onde deseja-se realizar a soma
Exemplos:
>> l = [1,2,2,4,8]
>> funcao_auxiliar1(l,’dir’) #nome generico nao use esse nome
>> l
[1,0,4,4,8]
>> l2 = [1,2,2,4,8]
>> funcao_auxiliar1(l2,’esq’)
>> l2
[1,4,0,4,8] """

def somar_adjacentes(numeros, direcao):
    if direcao == "direita":
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

        print(somados)
        if numeros != somados:
            numeros = somados
            return True
        else:
            return False
    elif direcao == "esquerda":
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
        if numeros != somados:
            numeros = somados
            return True
        else:
            return False

