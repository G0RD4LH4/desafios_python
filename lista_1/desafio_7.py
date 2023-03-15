n_conta = int(input("Digite o numero da conta: "))
saldo = int(input("Digite o saldo: "))
debito = int(input("Digite o debito: "))
credito = int(input("Digite o credito: "))

def banco(n_conta, saldo, debito, credito):
    saldo_atual = saldo - debito + credito

    if(saldo_atual > 0):
        status_saldo = "Positivo!"
    else:
        status_saldo = "Negativo!"

    return print("Numero da Conta:", n_conta, "Saldo:", status_saldo)

banco(n_conta, saldo, debito, credito)