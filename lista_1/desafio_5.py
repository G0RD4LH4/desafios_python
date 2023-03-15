numero_1 = int(input("Digite o primeiro numero inteiro: "))
numero_2 = int(input("Digite o segundo numero inteiro: "))
numero_real = float(input("Digite um numero real: "))

def solucao_a(numero_1, numero_2):
    resultado = (numero_1 * numero_1) + (numero_2 / 2)

    return resultado

def solucao_b(numero_1, numero_real):
    resultado = (numero_1 ** 3) + numero_real

    return resultado

def solucao_c(numero_real):
    resultado = numero_real ** 3

    return resultado

print("A:", solucao_a(numero_1, numero_2))
print("B:", solucao_b(numero_1, numero_real))
print("C:", solucao_c(numero_real))