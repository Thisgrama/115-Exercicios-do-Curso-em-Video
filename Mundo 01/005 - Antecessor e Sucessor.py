'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

num = int(input('Digite um número '))
print(f'O número \033[33m{num}\033[m tem o antecessor \033[036m{num-1}\033[m, e o sucessor \033[036m{num+1}\033[m')

# números são usados para cálculos então não usam aspas dentro dos parênteses
# com execeção de juntá-los ao invés de calculá-los.

# print(2 + 2)  
# >> 5

# print('2' + '2')  
# >> '22'

# print('2', '2')  
# >> '2 2'