''' Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''

lista = []
escolha = ''
while escolha != 'N':
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Você quer continuar[S/N]? ')).upper().strip()
    while escolha not in 'SN':
        escolha = str(input('Digite sim ou não [S/N]? ')).upper().strip()
par = [valor for valor in lista if valor % 2 == 0]
impar = [valor for valor in lista if valor % 2 == 1]
print(f'''
A lista completa: {lista}
A lista de pares: {par}
A lista de ímpares: {impar}
''')
