""" 
Defina uma função que dado um valor (iteravel) de tipo string, list ou tuple, um
potencial elemento (elem), e dois ı́ndices não negativos (ini e fim), devolva a quanti-
dade de vezes em que elem aparece no trecho de iteravel limitado por ini (inclusive)
e fim (exclusive).
Atenção elem pode não ocorrer em iterável. Lide com isso.
Atenção2: ini e fim podem n ao ser ındices existentes no
iteravel. Nesse caso considere apenas a parte de iteravel que possua ındices na faixa
[ini,fim[.
Importante!Não é para usar as funções pré definidas como list.count, por exemplo
Use o comando for para percorrer a estrutura de entrada e calcular o resultado.
"""

def contar_elem(valores,elem,ini,fim):
 
 #Verificando se "ini" existe em valores
 if ini not in valores:
  ini_posicao = 0
 
 #procurando "ini"
 else:
  cont = 0
  for valor in valores:
   if valor == ini:
    ini_posicao = cont
    break
   cont += 1
 
 #verificando se "fim" existe em valores
 if fim not in valores:
   fim_posicao =  len(valores) - 1
 
 #procurando "fim""
 else:
  cont = 0
  for valor in valores:
   if valor == fim:
    fim_posicao = cont
    break
   cont += 1
 
 #percorrendo os valores
 #contando os "elems"
 cont = 0
 for index in range(ini_posicao,fim_posicao + 1):
   if valores[index] == elem:
    cont += 1
    
 return cont
        
"""
Em programanção, usamos o conceito máscara para indicar informações que po-
dem ser mostradas ao usuário e informações que devem ser ”mascaradas”, isto e,
escondidas. Numa implementação de um jogo da forca, usamos uma máscara para
indicar que posições da palavra secreta o jogador já acertou, e cujo conteúdo por-
tanto deve ser mostrado ao jogador, e que posições devem continuar escondidas.
    Cada vez que o jogador acerta uma letra da palavra oculta, a máscara e atualizada
de forma a ficar com tracinhos nos lugares de letras que o jogador ainda não acertou
e mostrar, no seu devido lugar, as letras que ele já acertou.
Por exemplo, se a palavra for ”carta”, a máscara atual for: [’-’, ’a’, ’-’, ’-’, ’a’] e o
jogador adivinhar a letra ”t”,a máscara deveria ser atualizada para: [’-’, ’a’, ’-’, ’t’,
’a’].
    Escreva uma função chamada atualiza mascara que recebe como entrada uma
string contendo a palavra secreta (no exemplo acima, essa palavra seria “carta”),
uma lista cujos elementos são os caracteres da máscara atual (no exemplo acima [‘-
’,‘a’,‘-’,‘-’,‘a’ ], e uma string com a letra que ele acabou de escolher. Sua função deve
atualizar a máscara, colocando a letra escolhida no seu devido lugar (caso esteja
na palavra). Se a letra não estiver na palavra, a máscara não deve ser modificada.
A função não terá valor de retorno.
"""

def atualiza_mascara(palavra_secreta, letra):
    palavra_mascarada = []
    for posicao in palavra_secreta:
        if posicao == letra:
            palavra_mascarada.append(letra)
        else:
            palavra_mascarada.append("-")
    return palavra_mascarada

