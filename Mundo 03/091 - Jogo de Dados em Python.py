'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

from operator import itemgetter
from random import randint
from time import sleep

dicionario = {}
for i in range(1,5):
    dicionario[f'Jogador {i} jogou:'] = randint(1,6)
    print(f'Jogador {i} jogou:',dicionario[f'Jogador {i} jogou:'])
    sleep(1)
ranking = sorted(dicionario.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking): print(f'{i+1}° lugar: {v[0]} {v[1]}')