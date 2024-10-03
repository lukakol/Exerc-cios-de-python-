# Solicita ao usuário que insira uma resposta à pergunta "Você quer namorar comigo?"
n = input('Você quer namorar comigo? ').strip().upper()

# Verifica se a resposta do usuário é "SIM"
if n == 'SIM':
    # Se a resposta for "SIM", imprime "Que bom!"
    print('Que bom!')
else:
    # Se a resposta não for "SIM", imprime "Nem queria mesmo"
    print('Nem queria mesmo')
