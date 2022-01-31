
""" 
Ilustração
lista = ['Ian', 80kg]
           0      1
"""
cadastro = []
dados = []

mai = 0
men = 0
x = 0

resposta = 's'

print('----------CADASTRO DE PESSOAS----------')

while resposta == 's': 
    resposta = input("Deseja cadastra uma pessoa? [s/n] ")
    if resposta == 'n':
        break
    elif resposta != 's' and resposta != 'n':
        print('Resposta Inválida')
        break
    cadastro.append(str(input("Nome: ")))   
    if cadastro == float:
        print('Resposta inválida')
    cadastro.append(float(input("Peso (kg): ")))
    if x == 0:
        mai = cadastro[1]
        men = cadastro[1]
    else:
        if cadastro[1] >= mai:
            mai = cadastro[1]
        else:
            men = cadastro[1] 
    dados.append(cadastro[:]) # Ligação entre o cadastro e os dados
    cadastro.clear
    x += 1

print(f'O total de pessoas cadastradas foram {x}')
print(f'O maior peso foi de {mai}kg, pertencente a ', end='')
for d in dados:
    if d[1] == mai:
        print(f'e [{d[0]}]', end='')
print()   
print(f'O menor peso foi de {men}kg, pertencente a ')
for d in dados:
    if d[1] == men:
        print(f'e [{d[0]}]', end='')
print()