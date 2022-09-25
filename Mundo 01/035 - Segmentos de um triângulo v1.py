'''Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.'''

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
s = (s1, s2, s3)
print(f'\033[1;36m{"Podem" if s1 + s2 + s3 - max(s) > max(s) else "Não podem"}\033[m formar um triângulo')

# style 0 normal, 1 negrito, 4 sublinhado e 7 invertido
# text 30 branco, 31, vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 ciano e 37 cinza
# back 40   ''             ''        ''        ''          ''      ''        ''     47  ''