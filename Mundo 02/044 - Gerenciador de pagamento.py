'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de total

– à vista no cartão: 5% de total

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juro'''

produto = float(input('Digite o preço do produto: R$'))
pagamento = int(input('''Qual a forma de pagamento? 
1 = à vista no dinheiro ou cheque
2 = à vista no cartão
3 = 2x no cartão
4 = 3x ou mais no cartão
Digite a opção: '''))

if pagamento == 1: total = produto - produto * 0.10
elif pagamento == 2: total = produto - produto * 0.05
elif pagamento == 3:
    total = produto
    print(f'2x de {produto/2}')
elif pagamento == 4:
    total = produto * 1.20
    parcela = int(input('Em quantas parcelas? '))
    print(f'{parcela}x de R${total/parcela:.2f}')
else: print('Nenhuma opção digitada, tente novamente.')
print(f'O preço ficou: {total:.2f}')