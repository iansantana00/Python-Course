import primeiro

# Módulo importado irá ler:
# primeiro.py foi importado.
# Geek University - primeiro.py

def funcao2():
    primeiro.funcao1()

if __name__ == '__main__':
    funcao2()
    print('segundo.py está sendo executado diretamente.')
else:
    print(f'segundo.py foi importado. {__name__}')
    