ano = int(input("Digite o ano: "))
mes = int(input("Digite o mes: "))
dia = int(input("Digite o dia: "))

def conversao(dia, mes, ano):
    ano = (2023 - ano) * 365
    mes = mes * 30

    resultado = ano + mes + dia

    return resultado

print("Idade em dias:", conversao(dia, mes, ano), "dias.")