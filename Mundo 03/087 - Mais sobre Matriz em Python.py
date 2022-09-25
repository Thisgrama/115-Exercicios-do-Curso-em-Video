''' Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
soma_terceira_coluna = 0

for linha in range(0, 3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor para {linha, coluna}: '))

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0: soma_par += matriz[l][c]
    print()
    soma_terceira_coluna += matriz[l][2]

maior_valor_segunda_linha = max(matriz[1])
print(f'''
A soma de todos os valores pares digitados é: {soma_par}
O maior valor da segunda linha é: {maior_valor_segunda_linha}
A soma dos valores da terceira coluna é: {soma_terceira_coluna}
''')