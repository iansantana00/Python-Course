"""Continuação ..."""

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('----------------------------')

nome = 'Geek University'
for letra in nome:
    print(letra, end= "") # Utiliza o end="" para fazer a leitura sem pular linha 

print('-----------------------------')

# Dá para usar a string com operações aritméticas
nome = "Geek"
print(nome + 'University')
