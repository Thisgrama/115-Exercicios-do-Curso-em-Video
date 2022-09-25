'''Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(largura, comprimento):
    return largura * comprimento

largura = float(input('Digite a largura em metros: '))
comprimento = float(input('Digite o comprimento em metros: '))
print(f'A área de um terreno {largura} x {comprimento} é de {area(largura, comprimento)} m²')