'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar 
ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date

while True:
    gênero = input('Digite o seu gênero: m(Masculino) ou f(femínino)')
    if gênero == 'm':
        nascimento = int(input('Digite o ano do seu nascimento: '))
        idade = date.today().year - nascimento
        if idade == 18: print('Você deve se alistar esse ano!')
        elif idade < 18: print(f'Ainda faltam {18 - idade} ano(s) para você se alistar.')
        elif idade > 18: print(f'Você já deveria ter se alistado {idade - 18} ano(s) atrás')
        break
    elif gênero == 'f': 
        print('Mulheres não precisam se alistar')
        break
    else:
        print('Nenhuma das opções digitadas, tente novamente')