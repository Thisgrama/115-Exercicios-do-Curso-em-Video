'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n = int(input('Digite um número '))
print(f'Com base no número {n}\nO dobro é {n*2}\nO triplo é {n*3}\nE a raiz quadrada {n**(1/2):.3f}')

# caso eu não use a variavel depois, eu posso colocar o valor dela aonde vou usar, economizando espaço
# potencia é **
# raiz quadrada é a potencia 1/2
# eu poderia calcular a potência com pow(n, 1/2)
# o :3.f definiu que o máximo de caracteres é 3 pontos flutuantes(casas decimais)