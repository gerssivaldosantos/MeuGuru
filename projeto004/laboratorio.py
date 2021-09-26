"""Escreva um programa em Python que leia uma s´erie de lan¸camentos de um dado, guarde-os numa lista,
e conte o n´umero de ocorrˆencias de s´eries de faces repetidas. Observe os exemplos a seguir:
Suponha que foram fornecidos os seguintes n´umeros na sequˆencia de lan¸camentos do dado:
4 5 4 2 1 4 4 1 1 3 5 1 2 3 1
Nesse caso, o seu programa deve gerar como sa´ıda o n´umero dois (n´umero de s´eries de faces repetidas).
Vejamos outro exemplo:
3 5 4 3 3 1 3 1 1 1 1 2 5 1 6
Novamente o seu programa deve gerar como sa´ıda o n´umero dois, correspondendo `a s´erie de faces trˆes
e `a s´erie de faces um. Observe que o tamanho da s´erie n˜ao ´e importante, a sa´ıda do seu programa ´e
apenas o n´umero de s´eries registradas."""


def ler_faces(qnt_jogadas):
	"""Recebe do usuário a quantidade
	de jogadas dadas como parâmetro e
	retorna uma lista com as jogadas
	
	int -> list
	"""
	jogadas = []
	
	while len(jogadas) < qnt_jogadas:
		jogada = int(input("Digite um numero entre 1 e 6 : "))
		if jogada >= 1 and jogada <= 6:
			jogadas.append(jogada)
			print(f"{len(jogadas)}° face registrada !")
		else:
			print("Número inválido. ",end="")
	return jogadas
	
	
def encontrar_repetidos(jogadas):
	""" Recebe uma lista de jogadas e conta
	quantas series de numeros adjacentes iguais
	ocorrem nas faces dos dados jogados
	
	list -> int """
	series = 0
	inicio_serie = None
	
	for i in range(len(jogadas)-1):
		numero = jogadas[i]
		prox_num = jogadas[i + 1]
		
		if numero == prox_num:
			if numero != inicio_serie:
				inicio_serie = numero
				series += 1
		if numero != inicio_serie:
			inicio_serie = numero
			
	return series
			
		
		
def main():
	qt = int(input("Fazer quantas jogadas ? :"))
	jogadas = ler_faces(qt)
	
	print(encontrar_repetidos(jogadas))

main()
	
    





