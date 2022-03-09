
escrita = ''

with open('arq.txt', 'w', encoding='utf-8') as texto:
    while escrita != '0':
        escrita = input('Escreva: ')
        texto.write(escrita)
        texto.write('\n')

with open('arq.txt', 'r', encoding='utf-8') as texto:
    print(texto.read())