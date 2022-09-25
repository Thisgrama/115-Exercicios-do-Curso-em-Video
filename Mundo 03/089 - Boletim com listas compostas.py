'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um 
e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista = []
escolha = ''
while escolha != 'N':
    nome = str(input('Digite o nome do aluno: ')).strip().title()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    lista.append([nome, nota1, nota2])
    escolha = str(input('Deseja continuar[s/n]? ')).upper()
    while escolha not in 'SN': escolha = str(input('Digite uma opção válida[s/n]: ')).upper()

print(f'\n{"N°":<4}{"Nome":<10}{"Média":>8}')
for i in range(0, len(lista)):
    print(f'{i:<4}{lista[i][0]:<10}{(lista[i][1] + lista[i][2]) / 2:>8}')

while True:
    opçao = str(input('Deseja ver a nota de algum aluno[s/n]? ')).strip().title()
    if opçao == 'N': break
    elif opçao == 'S':
        numero = int(input('Digite o número do aluno: '))
        if numero <= len(lista) - 1:
            print(f'O aluno {lista[numero][0]} teve as notas {lista[numero][1]} e {lista[numero][2]}')
        else:
            print('Digite um número valido')
    else:
        print('Digite uma opção válida')
    