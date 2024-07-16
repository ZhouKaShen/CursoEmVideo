valor = float(input("Digite um valor em reais: "))
desconto = valor - valor * 0.05
print("O desconto de 5% no valor de R${:.2f} é de: R${:.2f}".format(valor, desconto))
