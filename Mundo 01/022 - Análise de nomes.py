'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite o seu nome completo: ')).strip() # strip() remove os espaços desnecessários antes e depois das palavras
# outra funcionalidade é nome.rstrip() remove os espaços da direita, nome.lstrip() remove os espaços da esquerda

print('Analisando o seu nome...')
print('Seu nome todo em maiúsculo é:', nome.upper()) # transforma a string em maiúsculo
print('Seu nome todo em minúsculo é:', nome.lower()) # transforma a string em minúsculo
print(f'Seu nome tem {len(nome.replace(" ", ""))} letras') # replace substituiu o espaço por nada.
# len(nome) exibe o comprimento da variavel
separa = nome.split() # divide as palavras de uma frase, 'Thiago Santos Silva' fica 'Thiago' 'Santos' 'Silva'
print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')

# nome[0][2], mostra a terceira(0-2) letra da primeira palavra, 'i'
# string é imutável
# '-'.join(palavra) junta a string na palavra, 'computador-e-celular'