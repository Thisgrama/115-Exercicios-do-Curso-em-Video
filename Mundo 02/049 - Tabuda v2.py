''''Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.'''''

n = int(input('Tabuada de: '))
print('-' * 10)
for i in range (1, 11):
    print(n, 'x', i, '=', n * i)
print('-' * 10)