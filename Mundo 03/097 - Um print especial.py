'''Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(texto):
    print('~' * (len(texto) + 4) + f'\n  {texto}\n' + '~' * (len(texto) + 4))

escreva(str(input('Digite um texto: ')))