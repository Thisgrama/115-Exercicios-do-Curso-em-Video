'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.'''

from math import trunc
n = float(input('Digite um número: '))
print(f'Sua parte inteira é: {trunc(n)}')

# python tem um conjunto limitado de comandos e caso precise de uma função especifica é preciso importar
# usamos o comando import (nome da biblioteca) para importar toda a biblioteca
# caso seja necessário apenas uma coisa da biblioteca usa-se from (nome da biblioteca) import (comando especifico)
# por exemplo, (math) importa funções para expressões matemáticas
# o comando floor da biblioteca math, ele arredonda os números pra baixo, o ceil arredonda pra cima
# nem sempre precisa-se importar, nesse projeto poderia-se usar o comando int(n) que transformaria o decimal em inteiro