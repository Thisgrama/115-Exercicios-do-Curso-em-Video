'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import datetime

maior = 0
menor = 0

for i in range(1, 8):
    nasc = int(input(f'Digite data de nascimento da {i}° pessoa: '))
    idade = datetime.today().year - nasc
    if idade >= 18: maior += 1
    elif idade < 18: menor += 1
print(f'Temos {maior} pessoas maiores de idade')
print(f'Temos {menor} pessoas menores de idade')