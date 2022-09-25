'''Crie um programa que faça o computador jogar Jokenpô com você.'''

# importações necessárias

from random import choice
from time import sleep
import emoji


# emojis

Pedra = ':raised_fist:'
Papel = ':hand_with_fingers_splayed:'
Tesoura = ":victory_hand:"


# dados
você = input('Pedra, Papel ou Tesoura? ').title()
escolhas = ('Pedra', 'Papel', 'Tesoura')
computador = choice(escolhas)


# converter str para emoji

def emojicon(str):
    emo = Pedra if str == 'Pedra' else Papel if str == 'Papel' else Tesoura
    return emo

# exibir os emojis escolhidos imitando um jogo na vida real

print(emoji.emojize(f'''
{Pedra}    JO   {Pedra}
{Papel}    KEM  {Papel}
{emojicon(você)}    PÔ!!!   {emojicon(computador)}
'''))

sleep(1)

# resultado

print(f'Você escolheu {você} e o computador escolheu {computador}')

if você == 'Pedra' and computador == 'Tesoura' or você == 'Papel' and computador == 'Pedra' or você == 'Tesoura' and computador == 'Papel':
    resultado = 'ganhou.'
elif você == computador: resultado = 'empatou'
else: resultado = 'perdeu.'
print('Você', resultado)