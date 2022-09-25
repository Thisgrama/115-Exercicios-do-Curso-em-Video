'''Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.'''

# criei a variável nome e atribui a ela o comando input()
nome = input('Qual é o seu nome? ') # input tem a função de digitar fora do código
print(f'É um prazer te conhecer, \033[33m{nome}!\033[m')

# quando precisamos de uma variável no meio de uma str, utiliza-se f('Texto {variável} texto.')
# isso é útil para não tem que fazer assim: 
# ('Texto', nome, 'texto') >> Texto Thiago texto
# Ou ('Texto' + variável + 'texto) >> TextoThiagotexto
# use , para dar um espaço e + para juntar: ('Texto )

# para o python, toda variável é um objeto

# o = 'atribui valor' 
# print(o)
# >> atribui valor

# o == confere se é igual
# print(o)
# >> False

