'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

tupla = tuple(int(input('Digite valores '))for i in range(1, 5))
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla: print(f'O primeiro 3 apareceu na {tupla.index(3) + 1}° posição')
print('Os números pares foram:', {i for i in tupla if i % 2 == 0})