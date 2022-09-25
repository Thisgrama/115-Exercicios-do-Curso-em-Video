'''Refaça o exercício 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

n = int(input('Digite o número: '))
r = int(input('Digite a razão: '))
termo = n
contador = 1

while contador <= 10:
    print(termo, end =' >')
    termo += r
    contador += 1
print('Fim')