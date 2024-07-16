salario = float(input("Digite o salário do funcionário: R$"))

if salario > 1250:
    print("O salário com um aumento de 10% é de: \nR${}".format(salario + (salario * 0.10)))
else:
    print("O salário com um aumento de 15% é de: \nR${}".format(salario + (salario * 0.15)))

print("Fim do programa!")
