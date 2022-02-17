"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar / Açúcar Sintático), deixar a linguagem mais agradável

/----------------------------------------/
/       Function Decorator               /
------------------------------------------

------------------------------------------
/ /------------------------------------/ /
/ /     Função decorada                / /
/ /------------------------------------/ /
/----------------------------------------
"""

# Decorators como funções (Sintaxe não recomendada / Sem Açúcar Sintático)

def seja_educado(funcao): # Decorator
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo 

def saudacao(): # Função decorada
    print('Seja bem-vindo(a) à Geek University')

# Testando 1

# Executando a SOMENTE a Função saudacao()
saudacao() 

print('')

# Executando a Função saudacao() Decorada
teste = seja_educado(saudacao)

teste()

print('')

# Testando 2 

def raiva():
    print('Mas te odiei!')

raiva_educada = seja_educado(raiva)

raiva_educada()

print('')

# Decorators com Syntax Sugar (Açúcar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

# Testando

apresentando()

print('')

@seja_educado_mesmo
def despedida():
    print('Até amanhã!')

# Testando

despedida()

"""
Exemplo de Decoradores em WebSites

|-------------------------------------------------------
|  Home   |  Serviços  |  Produtos  |  Administrativo  |
--------------------------------------------------------

http://www.suaempresa.com.br/home

http://www.suaempresa.com.br/serviços

http://www.suaempresa.com.br/produtos

http://www.suaempresa.com.br/administrativo

# OBS: Não é códio funcional (Que funcione) é apenas exemplo

def checa_login(request):
    if not request.usuario:
        redirect('http://www.suaempresa.com.br/login')

def home(request):
    return 'Pode acessar home'

def serviços(request):
    return 'Pode acessar serviços'

def produtos(request):
    return 'Pode acessar produtos'

@checa_login
def admin(request):
    return 'Pode acessar admin'

"""

# OBS: Não confunda Decorator com Decorator Function