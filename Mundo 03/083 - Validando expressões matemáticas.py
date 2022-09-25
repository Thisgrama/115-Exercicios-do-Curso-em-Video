'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite a expressão com (): '))
lista = []
for parenteses in expressao:
    if parenteses in '(': lista.append('(')
    elif parenteses in ')':
        if len(lista) > 0: lista.pop()
        else: 
            lista.append(')')
            break
    

print('Sua expressão é válida' if len(lista) == 0 else 'Sua expressão é inválida')