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
        
valores = [4,9,1,5,8,5,10,11]
ini = 1
fim = 10
elem = 5

print(contar_elem(valores,elem,ini,fim))