''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

from datetime import date

dicionario = {}
dicionario['Nome'] = str(input('Digite seu nome: ')).strip().title()
dicionario['Nascimento'] = int(input('Digite seu ano de nascimento: '))
dicionario['Carteira de trabalho:'] = int(input('Digite a sua carteira de trabalho: '))
dicionario['Idade'] = date.today().year - dicionario['Nascimento'] 

if dicionario['Carteira de trabalho:'] != 0:
    dicionario['Ano de contratação'] = int(input('Ano de contratação: '))
    dicionario['Salário'] = float(input('Digite seu salário: R$ '))
    aposentadoria = dicionario['Ano de contratação'] + 35
    print(f'''Você tem {dicionario["Idade"]} anos de idade e vai se aposentar em {aposentadoria}''')