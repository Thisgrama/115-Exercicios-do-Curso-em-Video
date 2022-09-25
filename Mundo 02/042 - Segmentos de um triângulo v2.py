'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
s = (s1, s2, s3)
if s1 + s2 + s3 - max(s) > max(s):
    if s1 == s2 == s3: tipo = 'equilátero'
    elif s1 == s2 or s2 == s3 or s1 == s3: tipo = 'isósceles'
    else: tipo = 'escaleno'
    print(f'\033[1;36mPodem\033[m formar um triângulo')
    print(f'O tipo desse triângulo é: \033[1;36m{tipo}\033[m')
else: print(f'\033[1;36mNão podem\033[m formar um triângulo')
