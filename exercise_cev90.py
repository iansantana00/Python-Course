
aluno = dict() # ou {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-' * 30)

print(f'  - Nome é igual a {aluno["nome"]}')
print(f'  - Média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print('  - Situção é igual a aprovado')
else: 
    print('  - Situação é igual a reprovado')

print('-' * 30)
print('Verificando o dicionário:')
print(aluno)
for k, v in aluno.items():
    print(f'{k} = {v}')