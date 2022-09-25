'''Crie um programa que leia dois números e mostre a soma entre eles.'''

n1 = int(input('Digite o primeiro número '))
n2 = int(input('Digite o segundo número '))
# especifiquei a classe das variáveis n1 e n2 como número inteiro, senão elas seriam interpretada como string
print(f'A soma de {n1} com {n2} é {n1 + n2}!')

# usamos {} como alvo de substituição do format, facilitando a troca de informações baseadas em algoritimos
# usamos ('{}').format(variável) ou (f'{Variável}')

# int = -1, 0, 1, 2, 3, 4, 5...
# float = -1.0, 0, 1.0, 2.0, 3.0...
# bool = True e False (É importante que esteja em maiúsculo)
# string = 'tudo que estiver em aspas'