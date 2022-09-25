'''Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.'''

celsius = float(input('Informe a temperatura em °C: '))
print(f'A temperatura em fahrenheit é: {(celsius*9/5) + 32:.1f}°F')