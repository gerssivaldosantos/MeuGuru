""" Uma pista de kart permite 10 voltas para cada um dos6 corredores. 

    Faça uma função chamada melhor_volta que 
receba como entrada uma matriz 6X10 com os tempos em segundos dos corredores em cada volta. A função deve 
retornar uma tupla informando: De quem foi a melhor volta da prova, com qual tempo e em que volta. Assuma
que os corredores tem tempos diferentes (dica: use a função min)Obs: use números de 1 a 6 para os corredores 
e 1 a 10 para as voltas (não esqueça que em Python os índices começam com 0) """

"De quem foi a melhor volta da prova, com qual tempo e em que volta."

"corredor, tempo, volta"

def melhor_volta(matriz):

    menor_tempo = matriz[0][0]
    melhor_corredor = 1
    melhor_volta = 1

    for corredor in range(len(matriz)):
        for volta in range(len(matriz[0])):
            tempo = matriz[corredor][volta]
            if menor_tempo > tempo:
                menor_tempo = tempo
                melhor_corredor = corredor + 1
                melhor_volta = volta + 1


    return  melhor_corredor, menor_tempo, melhor_volta

print(melhor_volta( [ 
    [10,30,40,50,60,30,40,10,20,40],
    [10,30,40,50,60,30,40,10,20,40],
    [10,30,40,50,60,30,40,10,20,40],
    [10,30,40,50,60,30,40,10,20,40],
    [10,30,40,50,60,30,40,10,20,40],
    [10,30,40,50,60,30,40,10,20,40],
 ] ))