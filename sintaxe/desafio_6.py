fahrenheit = float(input("Digite uma temperatudo ( GRAUS Fahrenheit ): "))

def conversao(fahrenheit):
    calculo = 5 *((fahrenheit - 32) / 9)

    return calculo

print("Graus Celsius:", conversao(fahrenheit))