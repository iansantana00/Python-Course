
def criar_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular,
             'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor
    """
    Retorna o valor da atual da conta acrescido do valor depositado.
    """


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f"numero: {conta['numero']} \nsaldo: {conta['saldo']}")


conta1 = criar_conta('123-5', 'Ian', 250.0, 700.0)
deposita(conta1, 15.0)
extrato(conta1)
saca(conta1, 20.0)
extrato(conta1)
help(deposita)
print(deposita.__doc__)
