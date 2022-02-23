"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

dender init -> __init__()

Dunder > Dunder Undescore

# dunder repr -> Representação do objeto
def __repr__(self):

dir(object) # ver outros métodos
"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas 

    def __str__(self):
        return self.titulo
    
    def __repr__(self): # Fazer a representação quando aparecer no código.
        return f'{self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    def __del__(self):
       print('Um objeto do tipo Livro foi deletado da memória') # Se usar del irá retornar essa mensagem

    def __add__(self, outro):
        return f'{self} e {outro}'

    def __mul__(self, outro): # Realizar uma multiplicação do livro por um número 
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'

livro1 = Livro('Coding and Coding', 'Doctor Python', 200) # instânciar o livro
livro2 = Livro('Estuda y Estuda', 'Ian Santana', 300)

print(livro1) # Sem a representação esse código ler onde o objeto está alocado <__main__.Livro object at 0x0000011339560FD0>
print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)