'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

contador = media = maior = menor = 0 

r = 'S'
while r != 'N':
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar? (S/N) ')).upper()
    contador += 1
    media += num
    if contador == 1: maior = menor = num
    else:
        if num > maior: maior = num
        if num < maior: menor = num
print(f'Você digitou {contador} números e a média foi {media/contador}')
print(f'O maior foi {maior} e o menor {menor}')
