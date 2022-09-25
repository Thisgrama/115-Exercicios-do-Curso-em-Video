'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite o seu nome: ')).title().split()
print('O seu nome', 'tem silva' if 'Silva' in nome else 'não tem Silva') 

# palavra.title() transforma a primeira letra de cada palavra em maiúscula e o resto em minúscula