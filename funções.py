"""
Definindo Funções

- Funções são pequenos trechos de códigos que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, 
é bom fazer uma verificação para que a função seja simplificada. 

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
...
"""

# Exemplos de utilização de funções:

cores = ['verde', 'amarela', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

# cores.append('Avançada') # AttributeError
# print(curso) 

cores.clear()
print(cores)

# print(help(print))

# DRY -> Don´t Repeat Yourself - Não repita você mesmo / Não repita seu código.

# Mas então, como deifinir funções?