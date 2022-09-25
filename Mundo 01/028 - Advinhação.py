'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint

número = randint(0, 5) # randomiza os números inteiros
advinhe = int(input('Tente advinhar o número: '))
print('Você acertou!' if advinhe == número else 'Você errou! Eu pensei no número', número)