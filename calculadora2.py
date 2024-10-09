n1 = int(input('Primeiro valor: '))  # Solicita o primeiro valor ao usuário
n2 = int(input('Segundo valor: '))   # Solicita o segundo valor ao usuário
opcao = 0  # Inicializa a variável opcao com 0

while opcao != 5:  # Loop continua até que a opção 5 seja escolhida
    print('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa')  # Exibe o menu de opções
    opcao = int(input('Qual a sua opção? '))  # Solicita a opção do usuário
    
    if opcao == 1:  # Se a opção for 1
        soma = n1 + n2  # Calcula a soma dos dois números
        print(f'A soma de {n1} e {n2} é {soma}')  # Exibe o resultado da soma
    elif opcao == 2:  # Se a opção for 2
        multiplicacao = n1 * n2  # Calcula a multiplicação dos dois números
        print(f'A multiplicação de {n1} e {n2} é {multiplicacao}')  # Exibe o resultado da multiplicação
    elif opcao == 3:  # Se a opção for 3
        if n1 > n2:  # Verifica qual número é maior
            maior = n1
        else:
            maior = n2
        print(f'O maior número entre {n1} e {n2} é {maior}')  # Exibe o maior número
    elif opcao == 4:  # Se a opção for 4
        n1 = int(input('Digite o primeiro valor: '))  # Solicita um novo primeiro valor
        n2 = int(input('Digite o segundo valor: '))  # Solicita um novo segundo valor
    elif opcao == 5:  # Se a opção for 5
        print('Saindo do programa...')  # Mensagem de saída
    else:  # Se a opção for inválida
        print('Opção inválida. Tente novamente.')  # Mensagem de erro

print('Programa encerrado.')  # Mensagem final do programa
