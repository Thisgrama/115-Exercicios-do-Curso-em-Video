'''Crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
No final, mostre a lista ordenada na tela.'''

lista = []
for i in range(1,6):
    valor = int(input(f'Digite o {i} valor: '))
    if i == 1 or valor > lista[-1]: lista.append(valor)
    else:
        for pos in range(len(lista)):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
print(lista)