
def verificador():
    numero = float(input('Digite o número a ser verificado: '))
    if numero < 0:
        return '-1'
    elif numero == 0:
        return '0'
    return '1'

print(verificador())



