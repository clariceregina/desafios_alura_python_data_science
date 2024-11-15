# 1. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.

frase = str('Olá, esta é a frase número 01.')
print(frase)

# 2. Crie um código que solicite uma frase e depois imprima a frase na tela.

frase2 = str(input('Insira o seu nome completo: '))
print(f'Olá, {frase2}, prazer em conhecer-te!')

# 3. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.

frase_maiuscula = str.upper(input('Insira o seu nome completo: '))
print(f'Confira seu nome com todas as letras maiúsculas: {frase_maiuscula}')

# 4. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.

frase_minuscula = str.lower(input('Insira o seu nome completo: '))
print(f'Confira seu nome com todas as letras minúsculas: {frase_minuscula}')

# 5. Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.

frase_sem_espacos = str.strip('   Frase com Espaço     ')
print(f'Confira a frase sem espaço no início e no fim: {frase_sem_espacos}')

# 6. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.

frase_sem_espacos2 = str.strip(input('Insira o seu nome completo: '))
print(f'Confira seu nome: {frase_sem_espacos2}')

# 7. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.

frase_sem_espacos_minuscula = str(
    input('Insira o seu nome completo: ')).strip().lower()
print(f'Confira seu nome: {frase_sem_espacos_minuscula}')

# 8. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.

frase_e_por_f = str(input(
    'Insira a frase: Este é um exemplo excelente de como escrever textos recheados de letras \'e\': ')).replace('e', 'f')
print(f'Trocamos as letras \'e\' por \'f\', confira: {frase_e_por_f}')

# 9. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.

frase_a_por_arroba = str(input(
    'Insira a frase: A avó amava a arte abstrata, admirando as belas almas alinhadas à análise astuta: ')).replace('a', '@')
print(f'Trocamos as letras \'a\' por \'@\', confira: {frase_a_por_arroba}')

# 10. Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.

frase_s_por_cifrao = str(input(
    'Insira a frase: Sábias serpentes silenciosas serpenteiam suavemente sobre as sombrias sombras: ')).replace('s', '$')
print(f'Trocamos as letras \'s\' por \'$\', confira: {frase_s_por_cifrao}')
