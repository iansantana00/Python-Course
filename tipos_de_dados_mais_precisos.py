"""
int, str, float, List, Set, Dict, etc
"""

# Pesquisa a função de cada um

from typing import TypedDict, final
from typing import Final
from typing import Union
from typing import Literal
from typing import Protocol
"""
def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro('Ian'))

- Literal type
- Union
- Final
- Typed dictionaries
- Protocols

# Literal type


def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass



def calcula_v1(operacao: str, num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')

# !r serve para botar aspas no parâmetro que você passou



def calcula_v1(operacao: Literal['+', '-'], num1: int, num2: int) -> None:
    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    else:
        raise ValueError(f'Operação inválida {operacao!r}')


calcula_v1('+', 10, 7)
calcula_v1('-', 9, 3)
calcula_v1('*', 3, 5)


# Union


def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2
# a função retorna ou str ou int (Union)

    if resultado > 50:
        return f'O valor {resultado} é muito grande.'
    else:
        return resultado


# Final  -> cria uma constante

NOME: Final = 'Geek'

print(NOME)

NOME = 'University'

print(NOME)
"""

# final


@final
class Pessoa:
    pass


class Estudante():
    pass

    @final
    def estudar(self):
        print('Estou estudando...')


class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)

print(geek)

outro = CursoPython(algo='vai', coisa=True)

print(outro)


# Protocols

# Todos os objetos que seguirem esse protocolo terão um atributo em particular


class Curso(Protocol):
    titulo: str

# os objetos que seguirem esse protocolo terão o atributo título
# o objeto não importa, o que importa são os atributos ou métodos


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda:
    titulo = 'Oi'


v1 = Venda()
# c1 = Curso()
# c1.titulo = 'Programação em Python'


# estudar(c1)
estudar(v1)
