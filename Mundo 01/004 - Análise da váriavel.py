'''Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo 
e todas as informações possíveis sobre ele.'''

algo = input('Digite algo: ')
print('O tipo primitivo deste valor é:', (type(algo)))
print('Só tem espaços?', algo.isspace())
print('Só tem números?', algo.isnumeric())
print('Só tem letras?', algo.isalpha())
print('Tem letras e números?', algo.isalnum())
print('Está em maiúsculas?', algo.isupper())
print('Está em minúsculas?', algo.islower())
print('Está capitalizada?', algo.istitle())


# type(variável) retorna algo classe
# is = é
# os parenteses depois dos is transformou o valor em bool, True e False