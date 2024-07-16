"""from math import trunc

n = float(input("Digite um número: "))
valor = trunc(n)

print("O número {} tem a parte inteira {}.".format(n, valor))"""

n = float(input("Digite um número: "))
print("O número {} tem a parte inteira {}".format(n, int(n)))
print("O número {} tem a parte inteira {:.0f}".format(n, n))
