'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

produto = float(input('Qual o preço do produto? R$'))
print(f'O produto que custava R${produto} com 5%" de desconto vai custar: R${produto - produto*0.05:.2f}')