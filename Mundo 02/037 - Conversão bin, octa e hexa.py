'''Escreva um programa em Python que leia um número inteiro qualquer 
e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

número = int(input('Digite um número inteiro: '))
while True:
    conversão = input('Digite a conversão desejada(binário, octal e hexadecimal): ')
    if conversão == 'binário':
        convertido = bin(número)
        break
    elif conversão == 'octal':
        convertido = oct(número)
        break
    elif conversão == 'hexadecimal':
        convertido = hex(número)
        break
    else:
        print('Você não digitou nenhuma das opções, tente novamente.')
print(f'O número {número} convertido para {conversão} é:', convertido[2:] if número > 0 else convertido[3:])