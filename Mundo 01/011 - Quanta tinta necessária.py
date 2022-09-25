'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'''Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m².
Para pintar essa parede você precisará de {(largura * altura)/2:.2f}l de tinta.''')