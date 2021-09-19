""" 
(4) Modifique a função acima de maneira que ela receba mais um parâmetro, a extrem-
idade que se deseja juntar.
Exemplo:
>> l = [0,1,2,2,4,0]
>> funcao_auxiliar2(l, ’dir’) #nome generico nao use esse nome
[0,0,1,2,2,4]
>> funcao_auxiliar2(l, ’esq’)
[1,2,2,4,0,0] """


def mover_zeros(numeros, direcao):
    if direcao == "esquerda":
        zeros = []
        outros = []
        for numero in numeros:
            if numero == 0:
                zeros.append(numero)
            else:
                outros.append(numero)
        numeros = []
        for numero in zeros:
            numeros.append(numero)
        for numero in outros:
            numeros.append(numero)

    elif direcao == "direita":
        zeros = []
        outros = []
        for numero in numeros:
            if numero == 0:
                zeros.append(numero)
            else:
                outros.append(numero)
        numeros = []
        for numero in outros:
            numeros.append(numero)
        for numero in zeros:
            numeros.append(numero)
    
    return numeros

print(mover_zeros())

