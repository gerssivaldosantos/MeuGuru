""" 
(3) Crie uma função que dado uma lista numérica de tamanho qualquer, junte todos
os elementos diferentes de zero no extremo direito da lista.
Exemplo:
>> l = [1,2,2,4,0]
>> funcao_auxiliar2(l) #nome generico nao use esse nome
>> l
[0,1,2,2,4] """

def mover_zeros(numeros):
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

