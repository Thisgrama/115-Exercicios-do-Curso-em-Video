'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []
maior = []
menor = []
for posição in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {posição}: ')))
for posi, valores in enumerate(lista):
    if valores == max(lista): maior.append(posi)
    if valores == min(lista): menor.append(posi)
print(lista)
print(f'''O maior valor digitado foi {max(lista)} na posição {maior} 
O menor foi {min(lista)} na posição {menor}''')