'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

from datetime import date

nascimento = int(input('Em que ano você nasceu? '))
idade = date.today().year - nascimento
if idade <= 9: categoria = 'Mirim'
elif 9 <= idade < 14: categoria = 'Infantil'
elif 14 <= idade < 19: categoria = 'Junior'
elif 19 <= idade < 25: categoria = 'Sênior' 
elif idade >= 25: categoria = 'Master'
print('Sua categoria é:', categoria)