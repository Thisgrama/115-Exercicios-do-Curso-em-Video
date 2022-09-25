'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

n = float(input('Uma distância em metros: '))

print(f'''A medida de {n}M:
Em kilômetros: {n * 0.001}Km.
Em hectômetro: {n * 0.01}Hm.
Em decâmetro: {n * 0.1:.1f}Dam.
Em decímetro: {n * 10:.0f}Dm.
Em centímetros: {n * 100:.0f}Cm.
Em milímetros: {n * 1000:.0f}Mm.''')

# '''
# aspas triplas permitem estender a string para mais de uma linha
# '''