'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*valores):
    print('Dados os números:')
    for valor in valores:
        print(valor, end =' ')
    print(f'\nForam informados {len(valores)} valores e o maior é: ', end='')
    m = 0
    for v in range(len(valores)):
        if valores[v] > m: m = valores[v]
    print()
    return m

maior(2, 50, 3, 6, 10, 20, 40, 39, 29, 49, 20, 10)
maior()
