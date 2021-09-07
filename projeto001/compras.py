"""
    Escreva uma função chamada total que recebe uma lista de compras e um dicionário contendo o 
preço de cada produto disponível em uma determinada loja, e retorna o valor total dos itens da 
lista que estejam disponíveis nesta loja. 

    Por exemplo, para os dados: 

lista de compras = ["biscoito", "chocolate", "farinha" ]

produtos = ["amaciante":4.99, "arroz":10.90, "biscoito":1.69, "café":6.98, "chocolate":3.79, "farinha":2.99]

    O Valor retornado pela função será 8.47
"""


def total(lista_compras, lista_disponivel):
    preco_total = 0
    for item in lista_compras:
        """ Buscando a ocorrencia dos itens contidos na lista de compras em lista de disponiveis """
        if item in lista_disponivel.keys():
            """ Caso exista ocorrencia, fazendo somátoria dos valores """
            preco_total += lista_disponivel[item]
    return preco_total
