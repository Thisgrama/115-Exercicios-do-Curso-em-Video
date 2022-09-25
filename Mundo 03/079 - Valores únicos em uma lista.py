'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
escolha = ''
while escolha != 'N':
    valor = (int(input('Digite um valor: ')))
    if lista.count(valor) == 1: print('Você já digitou esse valor.')
    else: lista.append(valor)
    escolha = (str(input('Quer continuar[s/n]? '))).upper().strip()
    while escolha not in 'SN':
        escolha = (str(input('Digite sim ou não[S/N]: '))).upper().strip()
        if escolha in 'SN': break
lista.sort()
print(f'Os valores digitados foram: \n{lista}')