'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

valor = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar? ')) * 12
prestação = valor / anos
minimo = salário * 0.3
if prestação <= minimo: resultado = f'aceito, você consegue pagar R${prestação:,.2f} por mês'
else: resultado = f'negado, a prestação de R${prestação:,.2f} excede 30%(R${minimo:,.2f}) do seu salário'
print(f'O empréstimo foi {resultado}')