'''Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distância = float(input('Qual a distância da sua viagem? '))
print(f'O preço da sua viagem vai ser: R$ {distância * 0.50 if distância <= 200 else distância * 0.45:.2f}')