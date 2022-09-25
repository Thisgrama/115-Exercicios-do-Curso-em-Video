'''Melhore o jogo do exercício 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, 
mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint

número = randint(0, 10)
advinhe = int(input('Tente advinhar o número: '))
palpite = 1

if advinhe == número: print('Parabéns! Você acertou de primeira!')
else:
    while advinhe != número:
        advinhe = int(input('Você errou. Tente novamente: '))
        if advinhe < número: print('Mais...')
        elif advinhe > número: print('Menos...')
        palpite += 1
    print(f'Você conseguiu advinhar na {palpite}° tentativa')