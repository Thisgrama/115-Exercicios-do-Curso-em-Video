'''Aprimore o exercício 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

lista = []
while True:
    jogadores = {}
    jogadores['Nome:'] = nome = str(input('Digite o nome do jogador: ')).strip().title()
    jogadores['Partidas:'] = partidas = int(input(f'Quantas partidas {nome} jogou? '))
    gols = []
    for partida in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na {partida}° partida? ')))
    jogadores['Gols:'] = gols
    lista.append(jogadores)
    while True: 
        continuar = str(input('Deseja continuar[S/N]? ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N': break
    if continuar == 'N': 
        jogadores = {}
        break
print('-'*20)
print(f'{"N°":<4}{"Nome":<10}{"Gols":<6}{"Total":>12}')
for jogador in range(len(lista)):
    print(f"{jogador:<4}{lista[jogador]['Nome:']:<10}{str(lista[jogador]['Gols:']):<6}{sum(lista[jogador]['Gols:']):>10}")
print('-'*20)
while True:
    continuar = str(input('Deseja ver algum jogador? ')).strip().upper()[0]
    if continuar == 'S' or continuar == 'N': break
    print('Digite S ou N: ')
while True:
    if continuar == 'N': break
    else:
        numero = int(input('Digite o número do jogador: ')) 
        while numero not in range(len(lista)): numero = int(input('Digite um número válido: '))
        print(f"O jogador {lista[numero]['Nome:']} jogou {lista[numero]['Partidas:']} partidas.")
        for partida in range(1, lista[numero]['Partidas:'] + 1): 
            print(f"    Na {partida}° partida fez {lista[numero]['Gols:'][partida-1]} gols")
        continuar = str(input('Deseja ver mais algum jogador?')).strip().upper()[0]
        if continuar not in 'SN': 
            while continuar not in 'SN': continuar = str(input('Digite uma opção válida [s/n]: ')).strip().upper()[0]