'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

ganhou = 'Você ganhou. O computador quer uma revanche'
perdeu = 'Você perdeu.'
c = 0
while True:
    num = int(input('Digite um número: '))
    par_impar = str(input('Par ou ímpar: ')).strip().upper()[0]
    com = randint(1, 10)
    soma = num + com
    print('=' * 10)
    print(f'Você digitou {num} e o computador {com}\nA soma é: {soma} o número é:', 'par' if soma % 2 == 0 else 'impar')
    print('=' * 10)
    if par_impar == 'P':
        if soma % 2 == 0: 
            print(ganhou)
            c += 1
        else: 
            print(perdeu)
            break
    elif par_impar == 'I':
        if soma % 2 == 1:
            print(ganhou)
            c += 1
        else:
            print(perdeu)
            break
print(f'Você ganhou {c} vezes')