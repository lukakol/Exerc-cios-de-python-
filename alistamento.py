from datetime import date  # Importa a classe date do módulo datetime
ano_atual = date.today().year  # Obtém o ano atual
ano_n = int(input('Em que ano você nasceu? '))  # Solicita ao usuário o ano de nascimento e converte para inteiro
idade = (ano_atual - ano_n)  # Calcula a idade do usuário
q_falta = idade - 18  # Calcula quantos anos faltam ou passaram dos 18 anos

print(f'Você nasceu em {ano_n} e tem {idade} anos')  # Exibe o ano de nascimento e a idade do usuário

if idade == 18:  # Verifica se a idade é exatamente 18 anos
    print('Você já pode se alistar!')  # Informa que o usuário pode se alistar
elif idade < 18:  # Verifica se a idade é menor que 18 anos
    print(f'Você não tem a idade mínima, ainda falta {q_falta} ano(s)')  # Informa quantos anos faltam para o alistamento
elif idade > 18:  # Verifica se a idade é maior que 18 anos
    print('Você ultrapassou a idade mínima, se aliste o mais rápido possível')  # Informa que o usuário já passou da idade de alistamento
elif ano_n == 0:  # Verifica se o ano de nascimento é 0 (o que não é possível)
    print('Por favor, digite uma idade válida')  # Solicita ao usuário que insira uma idade válida
