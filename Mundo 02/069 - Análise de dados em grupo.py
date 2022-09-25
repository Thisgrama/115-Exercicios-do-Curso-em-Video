'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.'''

mais = homens = mulheres= 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    genero = str(input('Digite o gênero da pessoa(M/F): ')).upper()
    continuar = str(input('Quer continuar(S/N)? ')).upper().strip()[0]
    if idade > 18: mais += 1
    if genero == 'M': homens += 1
    if genero == 'F' and idade < 20: mulheres += 1
    if continuar == 'N': break
print(f'{mais} pessoas com mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres com menos de 20 anos')