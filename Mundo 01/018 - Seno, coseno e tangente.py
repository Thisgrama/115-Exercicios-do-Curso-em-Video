'''Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo: '))
radiano = radians(angulo)
print(f'''O seno é: {sin(radiano):.2f} 
O coseno é: {cos(radiano):.2f} 
E a tangente é: {tan(radiano):.2f}''')

# sin calcula o seno, cos o cosseno e tan a tangente
# radians converteu o número em radiano para conseguir os valores corretos