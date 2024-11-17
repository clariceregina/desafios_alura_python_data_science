'''
'''


# 1. Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

numero1 = int(input('Insira um número inteiro: '))
numero2 = int(input('Insira o segundo número inteiro: '))

if numero1 < numero2:
    print(f'Os números inteiros entre {numero1} e {numero2} são: ')
    for inteiros in range(numero1 + 1, numero2):
        print(inteiros)
elif numero2 < numero1:
    print(f'Os números inteiros entre {numero2} e {numero1} são: ')
    for inteiros in range(numero2 + 1, numero1):
        print(inteiros)
else:
    print('Os números são iguais, dessa forma, não conseguimos imprimir uma sequência entre eles.')

# 2. Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

colonia_a = 4
colonia_b = 10

taxa_a = 0.03
taxa_b = 0.015

dias = 0

while colonia_a <= colonia_b:
    # colonia_a * (1 + taxa_a)
    colonia_a *= 1 + taxa_a
    colonia_b *= 1 + taxa_b
    dias += 1

print(f'A Colônia A levará {dias} dias para se igualar ou ultrapassar a Colônia B.\nColônia A = {
      colonia_a}\nColônia B = {colonia_b}')

# 3. Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(15):
    nota = float(input(f'Insira a nota da pessoa usuária {i}: '))

    while (nota < 0) or (nota > 5):
        nota = float(
            input(f'Nota inválida, insira novamente a nota da pessoa usuária {i}: '))

print('Verificação feita. Todas as notas são válidas')

# 4. Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

temperatura = float(input('Insira a temperatura em Celsius: '))

contadora = 0
soma = 0

while temperatura >= -273:
    soma += temperatura
    contadora += 1
    temperatura = float(input('Insira a temperatura em Celsius: '))

media = soma / contadora

print(f'A temperatura média é: {media}')

# 5. Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

numero_int = int(input('Informe um número inteiro: '))
fatorial = 1

i = numero_int
while i > 0:
    fatorial *= i
    i -= 1

print(f'Fatorial de {num} é {fatorial}')

### Momento dos projetos ###

# 6. Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

'''
Tabuada do 2:
2 x 1 = 2
2 x 2 = 4
[...]
2 x 10 = 20
'''

multiplicando = int(input('Insira um número inteiro de 1 a 10: '))

print(f'Tabuada do {multiplicando}')

for multiplicador in range(1, 11):
    produto = multiplicando * multiplicador
    print(f'{multiplicando} x {multiplicador} = {produto}')

# 7. Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

num = int(input('Informe um número inteiro positivo: '))

eh_primo = True

if num <= 1:
    eh_primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            eh_primo = False
            break
if eh_primo:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo!')
