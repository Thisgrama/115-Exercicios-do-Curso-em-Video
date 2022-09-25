'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

from random import choice

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))
alunos = [primeiro, segundo, terceiro, quarto] # [] cria listas
print(f'O aluno escolhido foi: {choice(alunos)}') # choices escolhe aleatoriamente um elemento no ()