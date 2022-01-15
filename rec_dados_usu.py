"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
- Aspas duplas;
- Aspas simples;
- Aspas simples triplas;
- Aspas duplas triplas;

"""

# Entrada de dados
#print("Qual o seu nome? ")
#nome = input() # Input -> Entrada | utilizando o dir e o comando __builtins__ (utilizar recursos)
nome = input('Qual a sua nome? ')

# Exemplo de print 'antigo' 2.x
# print("Seja bem-vindo(a) %s" % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}' .format(nome))

# Exemplo de print 'mais atual' 3.6
print(f'Seja bem-vido(a) {nome}')

#print("Qual a sua idade? ")
#idade = input()
idade = input("Qual a sua idade? ")
# Processamento

# Saída 

# Exemplo de print 'antigo' 2.x
# print("A %s tem %s anos" % (nome, idade)) 

# Exemplo de print 'moderno' 3.x
# print("{0} tem {1} anos".format(nome,idade))

# Exemplo de print 'mais atual' 3.6
print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para o outro. 

"""
print(f'A {nome} nasceu em {2021 - int(idade)}')

