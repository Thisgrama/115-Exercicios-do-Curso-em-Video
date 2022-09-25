'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.                                                           
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
escolha = ''
while escolha != 'N':
    lista.append(int(input('Digite um valor: ')))
    escolha = str(input('Você quer continuar[S/N]? ')).upper().strip()
    while escolha not in 'SN':
        escolha = str(input('Digite sim ou não [S/N]? ')).upper().strip()
lista.sort(reverse=True)
print(f'''
Foram digitados {len(lista)} números
A lista em ordem decrescente fica: {lista}
O valor 5 foi digitado? {"Sim" if 5 in lista else 'Não'}
''')