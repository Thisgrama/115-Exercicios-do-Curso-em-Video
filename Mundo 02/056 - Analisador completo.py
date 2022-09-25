'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''

media_idade = 0
nome_velho = ''
idade_velho = 0
menos_de_20 = 0

for pessoas in range(1, 5):
    print('='*5, f'{pessoas}° pessoa', '='*5)
    nome = (str(input('Nome: '))).title().strip()
    idade = (int(input('Idade: ')))
    genero = (str(input('Gênero(masculino ou feminino): '))).upper()
    media_idade += idade
    if genero == 'M':
        nome_velho = nome
        idade_velho = idade
        if idade > idade_velho:
            nome_velho = nome
            idade_velho = idade
    elif genero == 'F' and idade < 20:
        menos_de_20 += 1

print('A média de idade do grupo é:', media_idade / 4)
print('O homem mais velho se chama:', nome_velho)
print(menos_de_20, 'mulher com menos de 20 anos' if menos_de_20 == 1 else 'mulheres com menos de 20 anos')