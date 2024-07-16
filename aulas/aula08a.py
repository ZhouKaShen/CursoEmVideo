# import math
from math import sqrt, floor, ceil
num = int(input("Digite um número: "))
# raiz = math.sqrt(num)
raiz = sqrt(num)
print("{}".format(raiz))
print("A raiz quadradada de {} é igual a {:.2f}".format(num, floor(raiz)))
print("A raiz quadradada de {} é igual a {:.2f}".format(num, ceil(raiz)))

# Arredondamento para cima
# print("A raiz quadradada de {} é igual a {}".format(num, math.ceil(raiz)))

# Arredondamento para baixo
# print("A raiz quadradada de {} é igual a {}".format(num, math.floor(raiz)))