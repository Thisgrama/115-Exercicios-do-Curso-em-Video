'''Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

lista = []
while True:
    dicionario = {}
    dicionario['Nome'] = nome = str(input('Digite o nome da pessoa: ')).strip().title()
    dicionario['Idade'] = idade = int(input('Digite a idade da pessoa: '))
    while True:
        dicionario['Gênero'] = genero = str(input('Digite o seu gênero[M/F]: ')).strip().upper()[0]
        if genero == 'M' or genero == 'F': break
        print('Erro. Digite [M](masculino) ou [F](feminino):')
    lista.append(dicionario)
    while True:
        continuar = str(input('Deseja continuar[S/N]? ')).upper()[0]
        if continuar == 'S' or continuar == 'N': break
        print('Erro. Digite S(sim) ou N(Não)')
    if continuar == 'N': 
        dicionario = {}
        break

media = 0
for p in range(len(lista)): media += lista[p]['Idade']
media /= len(lista)

mulheres = [lista[mulher]['Nome'] for mulher in range(len(lista)) if lista[mulher]['Gênero'] == 'F']

acima_da_media = [lista[acima]['Nome'] for acima in range(len(lista)) if lista[acima]['Idade'] > media]

print(lista)
print(f'''
Foram cadastradas {len(lista)} pessoas
A média de idade foi: {media:.2f}
As mulheres da lista foram: {mulheres}
As pessoas com idade acima da média foram: {acima_da_media}
''')