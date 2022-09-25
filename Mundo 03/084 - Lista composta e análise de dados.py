'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

escolha = ''
lista = []
while escolha != 'N':
    nome = str(input('Digite o nome da pessoa: '))
    peso = int(input('Digite o peso da pessoa: '))
    lista.append([nome, peso])
    escolha = str(input('Deseja continuar[s/n]? ')).upper()
    while escolha not in 'SN': escolha = str(input('Digite uma opção válida[s/n]: ')).upper()
maior = max(p for n, p in lista)
menor = min(p for n, p in lista)
pesadas = [n for n, p in lista if p == maior]
leves = [n for n, p in lista if p == menor]

print(f'''
Foram cadastradas {len(lista)} pessoa(s)
A pessoa mais pesada foi: {pesadas} com {maior} Kg
A pessoa mais leve foi: {leves} com {menor} Kg
''')
