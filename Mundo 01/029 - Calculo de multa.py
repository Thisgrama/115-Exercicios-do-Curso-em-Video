'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Qual a velocidade atual do carro? '))
print(f'Você foi multado em {(velocidade-80)*7:.2f}, o límite permitdo é 80Km/h' if velocidade>80 else 'Você dirige com segurança.')