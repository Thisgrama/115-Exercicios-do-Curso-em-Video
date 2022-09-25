'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''

from random import sample
jogos = int(input('Quantos jogos você quer sortear? '))
for jogada in range(1, jogos + 1): print(f'Jogada{jogada}:', sorted(sample(range(1,60),6)))