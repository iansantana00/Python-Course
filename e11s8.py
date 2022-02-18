
def media(nota1, nota2, nota3, letra):
    return letra(nota1, nota2, nota3)

def letra_a(nota1, nota2, nota3):
    nota = (nota1 + nota2 + nota3) / 3
    return round(nota, 2)

def letra_p(nota1, nota2, nota3):
    nota = (nota1 * 5 + nota2 * 3 + nota3 * 2) / 10
    return round(nota, 2)

print('-------CÁLCULO DA MÉDIA DO ALUNO-------')
while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))
    if nota1 == str or nota2 == str or nota3 == str:
        print('Você digitou algum valor inválido!')
    else:
        break

print('-' * 40)

print('Deseja calcular qual tipo de média? ')
print('a - Média Aritmética')
print('p - Média Ponderada')    

print('')

while True:
    letra = input('Resposta: ')
    print('-' * 40)
    if letra == 'a':
        print('MÉDIA DO ALUNO: ')
        print(media(nota1, nota2, nota3, letra_a))
        break
    elif letra == 'p':
        print('MÉDIA DO ALUNO: ')
        print(media(nota1, nota2, nota3, letra_p))
        break
    print('Resposta Inválida')    
