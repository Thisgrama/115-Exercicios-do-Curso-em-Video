'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot # hypot = hipotenusa
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
print(f'O valor da hipotenusa é: {hypot(oposto, adjacente):.2f}')

# oposto ** 2 + adjacente ** 2 ** 1/2 = hypot