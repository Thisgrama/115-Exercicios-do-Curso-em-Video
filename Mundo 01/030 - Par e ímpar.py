'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

número = int(input('Digite um número: '))
print(f'O número {número} é', 'par' if número % 2 == 0 else 'ímpar')