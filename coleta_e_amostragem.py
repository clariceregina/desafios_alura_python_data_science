# Desafio: Coleta e amostragem de dados

# 1. Crie um programa que solicite à pessoa usuária digitar seu nome, e imprima “Olá, [nome]!”.
# Utilizei f-string

nome = str(input('Por favor, digite seu nome:\n'))
print(f'Olá, {nome}, prazer em te conhecer =)')

# 2. Crie um programa que solicite à pessoa usuária digitar seu nome e idade, e imprima “Olá, [nome], você tem [idade] anos.”.
# Utilizei operador de formatação

nome_1 = str(input('Digite seu nome, por favor:\n'))
idade_1 = int(input('Insira sua idade, por favor:\n'))
print('Olá, %s, legal saber que você tem %d anos.' % (nome_1, idade_1))

# 3. Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima “Olá, [nome], você tem [idade] anos e mede [altura] metros!”.
# Utilizei .format()

nome_2 = str(input('Digite seu nome, por favor:\n'))
idade_2 = int(input('Insira sua idade, por favor:\n'))
altura_2 = float(input(
    'Qual a sua altura em metros?\n(Por favor, utilize ponto ao invés de vírgula)\n'))
print('E aí, {}, que idade boa é {} anos, ein!? Gostei da sua altura de {} metros!'.format(
    nome_2, idade_2, altura_2))
