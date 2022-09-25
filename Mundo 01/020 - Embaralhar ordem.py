'''O mesmo professor do exercício 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))
ordem = [primeiro, segundo, terceiro, quarto]
shuffle(ordem) # embaralha os elementos()
print(f'A ordem vai ser: \n{ordem}')

# poderia ter usado o comando sample([p, s, t, q], 4)