import math  # Importa o módulo math, que contém funções matemáticas, incluindo sqrt para calcular a raiz quadrada.

num = int(input('Digite um número? '))  # Solicita ao usuário que digite um número e converte a entrada para um inteiro.

raiz = math.sqrt(num)  # Calcula a raiz quadrada do número fornecido pelo usuário.

print('A raiz de {} é {:.3f}'.format(num, raiz))  # Imprime o resultado formatado, mostrando a raiz quadrada com três casas decimais.
