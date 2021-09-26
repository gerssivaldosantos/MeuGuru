#jogo da forca
import random

def forca(mascara, erros):

    if erros == 0:
        print('----------')
        print('|        |')
        print('|        ')
        print('|        ')
        print('|        ')
        print('|        ')
    elif erros == 1:
        print('----------')
        print('|        |')
        print('|        o')
        print('|        ')
        print('|        ')
        print('|        ')
    elif erros == 2:
        print('----------')
        print('|        |')
        print('|        o')
        print('|        |')
        print('|        ')
        print('|        ')
    elif erros == 3:
        print('----------')
        print('|        |')
        print('|        o')
        print('|       /|')
        print('|        ')
        print('|        ')
    elif erros == 4:
        print('----------')
        print('|        |')
        print('|        o')
        print('|       /|\\')
        print('|        ')
        print('|        ')

    elif erros == 5:
        print('----------')
        print('|        |')
        print('|        o')
        print('|       /|\\')
        print('|       / ')
        print('|        ')
    else:
        print('----------')
        print('|        |')
        print('|        o')
        print('|       /|\\')
        print('|       / \\')
        print('|        ')
    print('---', end='\t')

    for el in mascara:
        print(el, end='')
    print('')


def sorteia_palavras():

    palavras = ['navio', 'carro', 'roupa', 'mato', 'motocicleta', 'cavalo']
    return random.choice(palavras)

def cria_mascara(palavra):

    mascara = []
    for i in range(len(palavra)):
        mascara.append('-')

    return mascara

def pega_letras(letras_antigas):

    letras_validas = list('zxcvbnmasdfghjklçqwertyuiop')
    letra = input('Digite uma letra para dar seu palpite: ')
    while (letra not in letras_validas) and (letra != '1') and (letra != '2') or (letra in letras_antigas):
        if letra in letras_antigas:
            letra = input('Essa letra, já foi chutada. Por favor dê outro palpite: ')
        else:
            letra = input('A letra digitada anteriormente não é válida, por favor tente novamente: ')

    if letra != '1' and letra != '2':
        letras_antigas.append(letra)
        
    return letra

def atualiza_mascara(mascara, palavra, letra):

    for i in range(len(palavra)):
        if letra == palavra[i]:
            mascara[i] = letra
    
def menu():

    print('Seja bem vindo ao Jogo da Forca')
    print('Digite 1 para sair')
    print('Digite 2 para reiniciar o jogo')
    print('Para jogar digite qualquer letra do alfabeto')

def main():

    menu()
    palavra = sorteia_palavras()
    mascara = cria_mascara(palavra)
    erros = 0
    acertos = 0
    forca(mascara, erros)
    letra = ''
    letras_antigas = []
    tam_palavra = len(palavra)
    while letra != '1':

        if erros > 5:
           print('Infelizmente você perdeu, digite 1 para sair, 2 para reiniciar')
        if acertos == tam_palavra:
            print('Parabéns, palavra descoberta. Digite 1 para sair, 2 para reiniciar')

        
        letra = pega_letras(letras_antigas)
        if letra == '2':
            #codigo para reiniciar o jogo
            print('*'*40)
            print('\nNovo jogo inicializado\n')
            print('*'*40, sep='')
            palavra = sorteia_palavras()
            mascara = cria_mascara(palavra)
            erros = 0
            acertos = 0
            letras_antigas = []
            tam_palavra = len(palavra)
            forca(mascara, erros)
            
        if letra !='2' and letra !='1' and erros < 6 and acertos < tam_palavra:
            if letra in palavra:
                atualiza_mascara(mascara, palavra, letra)
                acertos += 1
            else:
                print('Xiii, essa letra não pertence a palavra')
                erros += 1
    
            forca(mascara, erros)
      
main()






















        
