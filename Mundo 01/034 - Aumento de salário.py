''' Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

salário = float(input('Digite o salário do funcionário: R$'))
print(f'O novo salário é R${salário * 1.15 if salário <= 1250 else salário * 1.10:.2f}')