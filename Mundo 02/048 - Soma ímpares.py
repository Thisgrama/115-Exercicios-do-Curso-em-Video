'''Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
e que se encontram no intervalo de 1 até 500.'''

soma = 0
conta = 0
for m in range(3, 501, 2):
    if m % 3 == 0:
        soma += m
        conta += 1
print(f'A soma de {conta} ímpares múltiplos de três é:', soma)