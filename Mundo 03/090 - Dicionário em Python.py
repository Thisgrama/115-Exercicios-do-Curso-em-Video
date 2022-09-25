'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''

dicionario = {}
dicionario['Aluno'] = str(input('Digite o nome do aluno: ')).title().strip()
media = dicionario['Média'] = int(input(f'Digite a média do {dicionario["Aluno"]}: '))
dicionario['Situação'] = 'Aprovado' if media >= 7 else 'Reprovado' if media < 5 else 'Recuperação'
print('-' * 20)
for rotulo, valor in dicionario.items(): print(rotulo, 'é', valor)