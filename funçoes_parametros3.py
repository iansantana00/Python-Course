"""
CONTINUAÇÃO funçoes_parametros2.py...
"""

# Nomeando parâmetros (deve ser didático para o entendimento de quem usar seu código)

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de um função;

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

"""
 Argumentos nomeados (Keywor Arguments)  

Caso utilizemos nomes dos parâmetros nos argumentos para informá-los,
podemos utilizar qualquer ordem.
"""

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro comum na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total # NÃO SE DEVE USAR O return EMBAIXO DO if NESSE CASO

if __name__ == '__main__': # Se o nome do arquivo for igual a main(principal) então roda o arquivo diretamente
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))


if __name__ == '__main__':
    tupla = 1, 2, 3, 4, 5, 6, 7
    print(soma_impares(tupla))