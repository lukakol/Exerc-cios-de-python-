from time import sleep  # Importa a função sleep do módulo time, que permite pausar a execução do programa por um tempo especificado.

for c in range(10, -1, -1):  # Inicia um loop for que começa em 10 e vai até -1 (não inclusive), decrementando de 1 em 1.
    print(c)  # Imprime o valor atual de c.
    sleep(1)  # Pausa a execução do programa por 1 segundo.

print('Bum!')  # Após o loop terminar, imprime 'Bum!'.
