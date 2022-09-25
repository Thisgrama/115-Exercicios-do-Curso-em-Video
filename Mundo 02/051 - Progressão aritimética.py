'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''

n = int(input('Digite o número: '))
r = int(input('Digite a razão: '))
n10 = n + (10-1) * r

for i in range(n, n10 + r, r):
    print(i, end=' >')