velho = 0  # Acumulador da idade de pessoas mais velhas 
novo = 0  # Acumulador de pessoas mais novas
nome_velho = ''  # Acumulador da pessoa mais velha
sexo_velho = ''  # Acumulador do sexo das pessoas
total_idade = 0  # Acumulador da idade total 
totalmulher20 = 0  # Acumulador da quantidade de mulheres com menos de 20 anos

for c in range(1, 5):  # Vai fazer o loop 4 vezes
    print(f'------- {c}° pessoa ---------')  # Exibe o número da pessoa atual
    nome = input('Nome: ')  # Solicita o nome da pessoa
    idade = int(input('Idade: '))  # Solicita a idade da pessoa e converte para inteiro
    sexo = input('Sexo [M/F]: ')  # Solicita o sexo da pessoa
    
    total_idade += idade  # Adiciona a idade da pessoa ao total de idades
    
    if c == 1:  # Se for a primeira pessoa
        velho = idade  # Define a idade da primeira pessoa como a mais velha
        novo = idade  # Define a idade da primeira pessoa como a mais nova
        nome_velho = nome  # Define o nome da primeira pessoa como a mais velha
        sexo_velho = sexo  # Define o sexo da primeira pessoa como a mais velha
    else:
        if idade > velho:  # Se a idade da pessoa atual for maior que a idade mais velha registrada
            velho = idade  # Atualiza a idade mais velha
            nome_velho = nome  # Atualiza o nome da pessoa mais velha
            sexo_velho = sexo  # Atualiza o sexo da pessoa mais velha
        if idade < novo:  # Se a idade da pessoa atual for menor que a idade mais nova registrada
            novo = idade  # Atualiza a idade mais nova
        if sexo in 'Ff' and idade < 20: # Ff significa que pode ser o F ou f # Se a pessoa for do sexo feminino e tiver menos de 20 anos 
            totalmulher20 += 1  # Incrementa o contador de mulheres com menos de 20 anos

media = total_idade / 4  # Calcula a média das idades
print(f'A média das idades é {media} anos')  # Exibe a média das idades
print(f'A pessoa mais velha é {nome_velho}, com {velho} anos e do sexo {sexo_velho}.')  # Exibe a pessoa mais velha
print(f'A quantidade de mulheres menores de 20 é {totalmulher20}')  # Exibe a quantidade de mulheres com menos de 20 anos
