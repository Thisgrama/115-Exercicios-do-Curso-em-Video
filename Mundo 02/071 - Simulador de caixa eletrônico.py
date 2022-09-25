'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 40)
print('Banco do caralho')
print('=' * 40)

cinquenta = vinte = dez = um = 0
saque = int(input('Digite o valor a ser sacado: R$'))
while saque >= 50:
    cinquenta += 1
    saque -= 50
while saque >= 20:
    vinte += 1
    saque -= 20
while saque >= 10:
    dez += 1
    saque -= 10
while saque >= 1:
    um += 1
    saque -= 1
if cinquenta > 0: print(f'{cinquenta} cédulas de R$50')
if vinte > 0: print(f'{vinte} cédulas de R$20')
if dez > 0: print(f'{dez} cédulas de R$10')
if um > 0: print(f'{um} cédulas de R$1')