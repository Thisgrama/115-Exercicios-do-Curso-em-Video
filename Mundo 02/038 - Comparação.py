'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2: print(f'O {n1} é maior que {n2}')
elif n1 < n2: print(f'O {n2} é maior que {n1}')
elif n1 == n2: print(f'Não exite valor maior, {n1} e {n2} são iguais')