'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

p = str(input('Digite: ')).lower().strip()
print(f'A letra "a" aparece {p.count("a")} vezes') # conta quantas vezes o 'a' se repete na váriavel
print(f'A letra "a" aparece pela primeira vez na {p.find("a")+1} posição') # exibe onde achou o elemento 'a'
# (+1 foi adicionado porque o computador começa a contar do 0)
print(f'A letra "a" aparece pela última vez na {p.rfind("a")+1} posição') # exibe onde achou o elemento 'a' começando da direita

# p.count('a', 0, 5) exibe quantas vezes o 'a' se repete de 0 a 5
# p.find('a') quando não tem 'a' vai retornar -1