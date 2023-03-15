salario_atual = float(input("Digite o salario atual: "))
percentual = float(input("Digite o percentual: "))

def novo_salario(salario_atual, percentual):
    percentual = percentual / 100

    reajuste = (salario_atual * percentual) + salario_atual

    return print("Salario Reajustado: R$", reajuste)

novo_salario(salario_atual, percentual)