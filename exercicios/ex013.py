salario = float(input("Digite o salário do funcionário: R$"))
aumento_salario = salario + salario * 0.15
print("O reajuste do salário desse funciónario com 15% de aumento passa a receber de: R${:.2f}".format(aumento_salario))

preco_produto = float(input("Digite o preço do produto: R$"))
print("Preço original: R${:.2f}".format(preco_produto))

preco_vista = preco_produto - preco_produto * 0.10
print("Caso você pague à vista, será descontado 10% e o preço será de: R${:.2f}".format(preco_vista))

preco_parcelado = preco_produto + preco_produto * 0.10
print("Caso você pague parcelado, será cobrado 10% e o preço será de: R${:.2f}".format(preco_parcelado))
