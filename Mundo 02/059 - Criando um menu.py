''' Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
opção = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Digite a opção desejada: '''))

while opção != 5:
    if opção == 1: resultado = f'\nA soma de {primeiro} e {segundo} é: {primeiro + segundo}'
    elif opção == 2: resultado = f'\nA multiplicação de {primeiro} com {segundo} é: {primeiro * segundo}'
    elif opção == 3 and primeiro != segundo: resultado = f'\nO maior é: {primeiro if primeiro > segundo else segundo}'
    elif opção == 3 and primeiro == segundo: resultado = 'Os dois valores são iguais'
    elif opção == 4:
        primeiro = int(input('\nDigite o primeiro valor: '))
        segundo = int(input('\nDigite o segundo valor: '))
    print(resultado)
    opção = int(input('\nDigite a opção desejada: '))
print('\nFim do programa')