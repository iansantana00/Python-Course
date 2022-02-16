"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem todo iterator é um generator.

Outras Informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras)

-------------------------------------------------------------------------------------
| Funções                                 | Generator Functions                     |
-------------------------------------------------------------------------------------
| utilizam return                         | utilizam yield                          |
-------------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield múltiplas vezes    |
-------------------------------------------------------------------------------------
| quando executada, retorna um valor      | quando executada, retorna um generator  |
-------------------------------------------------------------------------------------
"""

# Exemplo Generator Function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador # Aguarda o next(), ele não acaba a execução como no return
        contador = contador + 1 

# OBS: Um Generator Function não é um Generator. Ele gera um Generator.

gen = conta_ate(5) # Gerou um Generator a partir da utilização da função conta_ate

print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('')

gen = conta_ate(10)

for num in gen: 
    print(num)

print('')

gen = conta_ate(3)

print(next(gen))

for num in gen:
    print(num)

# O loop for continua do next 

# Gerar todos os next de um vez

gen = list(conta_ate(2))

print(gen)