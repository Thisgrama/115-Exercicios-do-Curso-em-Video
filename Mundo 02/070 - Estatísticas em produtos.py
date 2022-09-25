'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

total = maior = menor = conta = 0
barato = ''
while True:
    print('=' * 40)
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$'))
    continuar = str(input('Deseja continuar(S/N)? ')).upper()[0]
    total += preço
    conta += 1
    if preço > 1000: maior += 1
    if conta == 1 or preço < menor:
        barato = nome
        menor = preço
    if continuar == 'N': break
print('O total gasto na compra foi: R$', total)
print(maior, 'produtos custam mais de R$1000')
print(f'O produto mais custou {menor} barato foi {barato}')