'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite seu nome completo: ')).title().strip().split()
n = list(nome) # transformou a classe str para list
print(f'Seu primeiro nome é: {n[0]}') # strings são divididas começando do 0
print(f'Seu último nome é: {n[-1]}') # exibe o último item da lista

# nome[0:3] = posição 0 a 3
# se houverem espaços entre as letras também será contado
# um terceiro número teria outra função nome[0:4:2] posição de 0 a 4, o último número define que vai pular as letras de 2 em 2
# nome[:7] começando do inicio até o 6(0-7)
# nome[7:] começando na 7°(6) string até o fim
# nome[2::2] começando do 2 até o fim, pulando de dois em dois
# nome[0][2], exibe a terceira[2](0-2) letra da primeira palavra[0]