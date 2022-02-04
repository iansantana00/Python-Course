"""
Erros mais comuns em Python

ATENÇÃO!
É importante prestar atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

' - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja, você escreveu algo que o Python
não reconhece como parte da linguagem.

Exemplos SyntaxError

a)

def funcao: 
    print('Geek University)

b) 

def = 1  # Palavra reservada como variável

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)

print(geek)

b)

geek()

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado. 

Exemplos TypeError

a)

print(len(5))

b)

print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um indice inválido.

Exemplos IndexError

a)

lista = ['Geek']
print(lista[2])

b)

lista = ['Geek']
print(lista[0][10])


5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento 
com tipo correto, mas valor inapropriado.

Exemplos ValueError

a)

print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

dic = {'python': 'university'}
python(dic['geek'])
 
7 - AttributeError -> Ocorre quando uma variável não tem atributo ou função.
 
a)

tupla = (2, 8, 92, 1, 3, 0)
print(tupla.sort())
# a função sort() não funciona em tupla, mas em lista e outros iteráveis

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

Exemplos IndentationError 

a)

def nova():
print('geek')

b)
for i in range(10):
       i + 1

OBS: Exceptions e Erros são sinônimos na programação
"""
