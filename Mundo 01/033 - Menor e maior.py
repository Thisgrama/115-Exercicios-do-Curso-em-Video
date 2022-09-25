'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

números = list(map(int, input('Digite o três números: ').split()))
print(f'O menor é {min(números)} e o maior é {max(números)}')

# min() menor max () maior