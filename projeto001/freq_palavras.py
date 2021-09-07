"""Construa uma função chamada freq_palavras(frases) que receba uma string e retorne um dicionário onde cada
palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece. Por exemplo

freq_palavras("dinheiro é dinheiro e vice versa")

Retorna o dicionário: {"dinheiro":2, "é":1, "e":1, "vice":1, "versa":1}"""

def freq_palavras(palavras):
    """ Primeiro eu transformo a string em uma lista para manipular melhor os dados e conseguir percorrer eles
    por um laço de repetição de maneira simplificada """
    lista_palavras = palavras.split()
    encontradas = []
    dicionario = {}
    for palavra in lista_palavras:
        if palavra not in encontradas:
            encontradas.append(palavra)
            """ Com o uso de uma lista auxiliar eu crio uma nova versão da lista original, com a diferença de que
            esta não contém palavras repetidas """
            dicionario.update({palavra:lista_palavras.count(palavra)})
            """ Fazendo uso da lista auxiliar, começo a popular um dicionário que usa a lista com palavras não repetidas
            como referencia, e a lista original como fonte de dado para contagem utilizando a função "count()" que recebe
            como parametro um valor dentro de uma lista e retorna a quantidade de ocorrencias desse valor na mesma """
    return dicionario

