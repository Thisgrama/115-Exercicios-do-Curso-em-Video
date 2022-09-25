'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''


lista = []

for p in range (1, 6): 
    lista.append(float(input(f'Digite o peso da {p}° pessoa: ')))
print(f'O maior peso foi {max(lista)}kg e o menor foi {min(lista)}kg')