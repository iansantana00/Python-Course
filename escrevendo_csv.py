"""
Escrevendo em arquivos CSV

reader(), (leitor), writer(), (escritor)

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV. Utilizamos o método
# writerow() para escrever cada linha. Este método recebe uma lista.


from csv import writer 

with open('filmes.csv', 'w', encoding='utf-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao]) 

# 'w' -> apaga se já existir, 'a' -> adiciona um novo arquivo 
"""

from csv import DictWriter

with open('filmes2.csv', 'a', encoding='utf-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader() # Escrever em dicionário
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow({"Título": filme, "Gênero": genero, "Duração": duracao})


