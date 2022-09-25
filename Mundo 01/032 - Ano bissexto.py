'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''

from datetime import date

ano = int(input('Digite o ano ou digite 0 para o ano atual: '))
ano = date.today().year if ano == 0 else ano # pega ano data do computador, date = modulo .today() = date de hoje .year = apenas o ano
print(f'O ano {ano} {"é" if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else "não é"} bissexto')