'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

tupla = ('Aprender', 'Python', 'Computador', 'Notebook')


for i in tupla:
    print(f'\nA palavra {i} temos as vogais: ', end= '')
    for letras in i:
        if letras.lower() in 'aeiou': print(letras, end=' ') 