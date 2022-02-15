"""
Dunder Name e Dunder Main

Dunder -> Double Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python, são utilizados dunder para criar funções, atributos, propriedade e etc... Utilizando
Double Under para não gerar conflito com os nomes desses elementos na programação.

# Na linguagem C, temos um programa da seguinte forma:

int main(){

    return 0;
}

# Na linguagem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}
"""

"""
from funçoes_parametros3 import soma_impares

Seu nome completo é Angelina Jolie
Seu nome completo é Jones Felicity
Seu nome completo é Angelina Jolie
Seu nome completo é Felicity Jones
Seu nome completo é Marcia Marques
16
16
"""
# Só com o import, o programa já lê todo o módulo
# inadequado, por isso deve solucionar com o __name__ e __main__ na origem do modulo

"""
from funçoes_parametros3 import soma_impares

Seu nome completo é Angelina Jolie
Seu nome completo é Jones Felicity
Seu nome completo é Angelina Jolie
Seu nome completo é Felicity Jones
Seu nome completo é Marcia Marques

# Não apareceu o soma_impares
"""

from funçoes_parametros3 import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6]))

# Diferença de quando importa o arquivo e o executa diretamente

import primeiro
import segundo

# primeiro.py
# segundo.py

# Se um arquivo python for executado diretamente será nomeado __main__
# Se um arquivo executado via importação será nomeado o próprio nome do arquivo

