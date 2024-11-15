# Desafio: Calculadora com Operadores

# 1. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.

numero1 = float(input('Insira o primeiro número: '))
numero2 = float(input('Insira o segundo número: '))
soma_n1_n2 = numero1 + numero2
print(f'O resultado da soma entre {numero1} e {numero2} é {soma_n1_n2}')

# 2. Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.

numero3 = float(input('Insira o primeiro número: '))
numero4 = float(input('Insira o segundo número: '))
numero5 = float(input('Insira o terceiro número: '))
soma_n3_n4_n5 = numero3 + numero4 + numero5
print(f'O resultado da soma entre {numero3}, {
      numero4} e {numero5} é {soma_n3_n4_n5}')

# 3. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.

numero6 = float(input('Insira o primeiro número: '))
numero7 = float(input('Insira o segundo número: '))
subtracao_n6_n7 = numero6 - numero7
print(f'O resultado da subtração entre os números {
      numero6} e {numero7} é {subtracao_n6_n7}')

# 4. Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.

numero8 = float(input('Insira o primeiro número: '))
numero9 = float(input('Insira o segundo número: '))
multiplicacao_n8_n9 = numero8 * numero9
print(f'O resultado da multiplicação entre os números {
      numero8} e {numero9} é {multiplicacao_n8_n9}')

# 5. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numero10 = float(input('Insira o primeiro número (numerador): '))
numero11 = float(
    input('Insira o segundo número diferente de 0 (denominador): '))
divisao_n10_n11 = numero10 / numero11
print(f'O resultado da divisão entre os números {
      numero10} e {numero11} é {divisao_n10_n11}')

# 6. Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.

numero12 = float(input('Insira o primeiro número: '))
numero13 = float(input('Insira o segundo número (expoente): '))
exponenciacao_n10_n11 = numero12 ** numero13
print(f'O resultado da exponenciação entre os números {
      numero12} e {numero13} é {exponenciacao_n10_n11}')

# 7. Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numero14 = float(input('Insira o primeiro número (numerador): '))
numero15 = float(
    input('Insira o segundo número diferente de 0 (denominador): '))
divisao_inteiro = numero14 // numero15
print(f'O resultado da divisão inteira entre os números {
      numero14} e {numero15} é {divisao_inteiro}')

# 8. Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.

numero16 = float(input('Insira o primeiro número (numerador): '))
numero17 = float(
    input('Insira o segundo número diferente de 0 (denominador): '))
divisao_resto = numero16 % numero17
print(f'O resultado da divisão entre os números {numero16} e {
      numero17} utilizando módulo é {divisao_resto}')

# 9. Crie um código que solicita 3 notas de um estudante e imprima a média das notas.

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
media_notas = (nota1 + nota2 + nota3) / 3
print(f'A média das notas é {media_notas} pontos.')

# 10. Crie um código que calcule e imprima a média ponderada dos números 5, 12, 20 e 15 com pesos respectivamente iguais a 1, 2, 3 e 4.
# Média Ponderada = ((nota1 × peso1) + (nota2 × peso2) + (nota3 × peso3)) ÷ (peso1 + peso2 + peso3)

nota4 = 5
nota5 = 12
nota6 = 20
nota7 = 15
media_ponderada = ((nota4 * 1) + (nota5 * 2) +
                   (nota6 * 3) + (nota7 * 4)) / (1 + 2 + 3 + 4)
print(f'A média ponderada das notas é igual a {media_ponderada}')
