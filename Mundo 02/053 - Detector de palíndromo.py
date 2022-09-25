'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:

APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

#for i in range(len(junto) -1, -1, -1):
#    inverso += junto[i]

print(f'O contrário de {frase} é:', inverso)
print('É' if junto == inverso else 'Não é', 'um palíndromo')