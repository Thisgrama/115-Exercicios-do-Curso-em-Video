'''Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cidade = str(input('Digite a cidade que você nasceu: ')).strip().capitalize().split() 
# capitalize transforma a primeira letra em maiúscula e o resto em minúscula
print('Começa com Santo?', 'Sim' if 'Santo' in cidade else 'Não') # Tem 'Santo' in(na) cidade(váriavel)