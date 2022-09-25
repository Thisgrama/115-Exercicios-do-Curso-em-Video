'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''


genero = str(input('Digite o seu gênero[M ou F]: ')).strip().upper()
while genero != 'M' and genero != 'F': 
    genero = str(input('Gênero invalido. Digite o seu gênero: ')).upper()
print('Tudo certo')

