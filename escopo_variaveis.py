"""
Escopo de variavéis

Dois caos de escopo:

1 - Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado a esse bloco.

Para declarar variáveis em Python:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C e em java:
int numero = 42
"""
numero = 42
# novo = 0

if numero > 10: 
    novo = numero + 10 # A variável 'novo' está declarada localmente dentro do bloco do if. Portanto, é local.
    print(novo)

print(novo)