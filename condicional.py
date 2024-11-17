# 1. Utilizando condição mais operador de maior/menor

nome_amizade = str(input('Insira o nome de uma amizade sua: '))
idade_amizade = int(input(f'Insira a idade de {nome_amizade}: '))
idade_pessoa = int(input('Insira a sua idade: '))
if idade_pessoa > idade_amizade:
    print(f'Que interessante! Você é mais velho(a) do que {nome_amizade}.')
elif idade_pessoa == idade_amizade:
    print(f'Que interessante! Você tem a mesma idade que {nome_amizade}.')
else:
    print(f'Que interessante! Você é mais novo(a) do que {nome_amizade}.')

# 2. Utilizando condição mais diferente de

nome_amizade2 = str(input('Insira o nome de uma amizade sua: '))
cor1 = str(input(f'Insira a cor favorita de {nome_amizade2}: '))
cor2 = str(input('Insira a sua cor favorita: '))
if cor1 != cor2:
    print(f'Você e {nome_amizade2} gostam de duas cores diferentes, mas igualmente bonitas: {
          cor1} e {cor2}.')
else:
    print(f'Vocês têm algo em comum: a cor favorita de vocês é {cor1}!')

# 3. Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

numero1 = float(input('Insira um número: '))
numero2 = float(input('Insira outro número: '))
if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}')
else:
    print(f'{numero2} é maior que {numero1}')

# 4. Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual = str(input('Insira o percentual de crescimento da empresa: '))
percentual = float(percentual.replace('%', '').replace('- ', '-'))

if percentual > 0:
    print(f'Uau! Com o percentual de {
          percentual}% a sua empresa está em crescimento! Parabéns!')
else:
    print(f'O crescimento negativo de {
          percentual}% não pode te desanimar. No próximo ano temos uma nova chance!')

# 5. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = input('Insira uma letra: ')
if len(letra) != 1:
    print(f'Você inseriu "{letra}", mas precisa digitar apenas uma letra.')
elif not letra.isalpha():
    print(f'Você inseriu "{
          letra}", que não é uma letra válida. Por favor, insira apenas uma letra do alfabeto.')
elif letra.upper() in ('A', 'E', 'I', 'O', 'U'):
    print(f'A letra {letra} é uma vogal.')
else:
    print(f'A letra {letra} é uma consoante.')

# 6. Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

modelo = str(input('Insira um modelo de carro: '))

ano1 = int(input('Insira o primeiro ano: '))
preco_ano1 = float(input(f'Insira o preço médio do {modelo} em {ano1}: '))

ano2 = int(input('Insira o segundo ano: '))
preco_ano2 = float(input(f'Insira o preço médio do {modelo} em {ano2}: '))

ano3 = int(input('Insira o terceiro ano: '))
preco_ano3 = float(input(f'Insira o preço médio do {modelo} em {ano3}: '))

maior_preco = preco_ano1
if preco_ano2 > maior_preco:
    maior_preco = preco_ano2
elif preco_ano3 > maior_preco:
    maior_preco = preco_ano3

menor_preco = preco_ano1
if preco_ano2 < menor_preco:
    menor_preco = preco_ano2
elif preco_ano3 < menor_preco:
    menor_preco = preco_ano3

print(f'O maior valor que o modelo {modelo} atingiu foi {
      maior_preco} e o menor foi {menor_preco}')

# 7. Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

p1 = float(input(f'Insira o valor do primeiro produto: '))
p2 = float(input(f'Insira o valor do segundo produto: '))
p3 = float(input(f'Insira o valor do terceiro produto: '))

if p1 < p2 and p1 < p3:
    print('O primeiro produto é o mais barato.')
elif p2 < p1 and p2 < p3:
    print('O segundo produto é o mais barato.')
elif p3 < p1 and p3 < p2:
    print('O terceiro produto é o mais barato.')
elif p1 == p2 == p3:
    print('Os três produtos possuem o mesmo valor.')
else:
    if p1 == p2:
        print('O primeiro e o segundo produto são os mais baratos.')
    if p2 == p3:
        print('O segundo e o terceiro produto são os mais baratos.')
    if p3 == p1:
        print('O terceiro e o primeiro produto são os mais baratos.')

# 8. Escreva um programa que leia três números e os exiba em ordem decrescente.

n1 = float(input(f'Insira o primeiro número: '))
n2 = float(input(f'Insira o segundo número: '))
n3 = float(input(f'Insira o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
    if n2 >= n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)

elif n2 >= n1 and n2 >= n3:
    print(n2)
    if n1 >= n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)

elif n3 >= n1 and n3 >= n2:
    print(n3)
    if n1 >= n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)

# 9. Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = str(input(
    'Em qual turno você estuda? Matutino, Tarde, Noite, Integral ou Ead?')).lower()
if turno == 'matutino':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
elif turno == 'integral':
    print('Bom dia, boa tarde e boa noite!')
elif turno == 'ead':
    print('O turno de quem estuda à distância acaba sendo \'quando dá\' né?!')
else:
    print('Opção inválida!')

# 10. Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

numero = int(input('Insira um número e te direi se é par ou ímpar: '))

if numero % 2 != 0:
    print('Este número é ímpar!')
else:
    print('Este número é par!')

# 11. Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

numero_ = float(input('Insira um número e te direi se é inteiro ou decimal: '))

if numero_ % 1 != 0:
    print('Este número é decimal!')
else:
    print('Este número é inteiro!')
