'''Escreva um programa que leia um número N inteiro qualquer
e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8'''

termo = int(input('Digite quantos termos você quer: '))
um = 0
dois = 1
if termo == 1: print(um)
elif termo == 2:
    print(f'{um} - {dois}', end = ' - ')
elif termo > 2:
    while termo != 0:
        total = um + dois
        print(total, end = ' - ')
        um = dois
        dois = total
        termo -= 1

print('Fim')