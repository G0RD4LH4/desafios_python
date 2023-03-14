nome_do_funcionario = input("Digite o nome do funcionado: ")
salario = float(input("Digite o salario: "))

reajuste = (salario * 0.10) + salario

print("Nome do Funcionario:", nome_do_funcionario, "| Salario Reajustado: R$", reajuste)