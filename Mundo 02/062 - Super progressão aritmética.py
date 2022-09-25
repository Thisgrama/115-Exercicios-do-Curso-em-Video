'''Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

n = int(input('Digite o número: '))
r = int(input('Digite a razão: '))
termo = n
contador = 0
total = 0
vezes = 10

while vezes != 0:
    total = vezes + total
    while contador <= total:
        print(termo, end =' >')
        termo += r
        contador += 1
    print(' Parou')
    vezes = int(input('Quantos termos você quer a mais? '))
print('Fim')