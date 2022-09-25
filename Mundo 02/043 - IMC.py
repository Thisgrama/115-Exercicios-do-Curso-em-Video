'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''

peso = float(input('Digite seu peso em kg: ')) 
altura = float(input('Digite sua altura em metros: ')) ** 2
imc = peso / altura
if imc < 18.5: status = 'abaixo do peso'
elif 18.5 <= imc < 25: status = 'com o peso ideal'
elif 25 <= imc < 30: status = 'com sobrepeso'
elif imc >= 40: status = 'com obesidade mórbida'
print(f'Seu imc é {imc:.1f}\nVocê está',  status)