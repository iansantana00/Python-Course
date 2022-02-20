"""
POO - Classes 

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatiza o controle das lâmpadas da sua casa.
Entretando, no Python não exite a o tipo lâmpada, mas somente o tipo inteiro, float, string, booleano,
list, set...
Deve-se criar então um tipo lâmpada.

Classes podem conter:
    - Atributos -> Represetam as características do objeto. Ou seja, pelos atributos conseguimos representar 
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente iríamos querer saber se a 
    lâmpada é 110v ou 220v, se ela é branca, amarela, vermelha ou outra cor, qual a luminosidade e etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode 
    realizar no seu sistema. No caso da lâmpada, por exemplo, um comportamento comum que muito provavelmente
    iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado e 
queremos botá-lo para ser executado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo
(entretanto, as classes internas do Python têm inicias minúscuals). Se o nome for composto, utiliza-se
as inicias de ambas as palavras em maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes
de classes, atributos, métodos, arquivos, diretórios e etc.

OBS: Quando estamos planejando um software e definimos quais classes temos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade.
"""

inteiro =  10 # class int(object)
string = 'Ian'
decimal = 11.23
verdade = True
vogais = 'a', 'e', 'i', 'o', 'u'

print(type(inteiro))
print(type(string))
print(type(decimal))
print(type(verdade))
print(type(vogais))

# Criando o tipo lâmpada:
class Lampada():
    pass

Lamp = Lampada()

print(type(Lamp))

class Int():
    pass

valor = int('42') # cast

print(help(int)) # verificar a classe python 


