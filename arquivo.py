
with open('palavras.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('banana\n')
    arquivo.write('melancia\n')
    arquivo.write('manga\n')
    arquivo.write('morango\n')

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
