n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro: "))
s = n1 + n2 # Soma
m =  n1 * n2 # Multiplicação
d = n1 / n2 # Divisão
di = n1 // n2 # Divisão inteira
e = n1 ** n2 # Potência
rq = s ** (1/2) # Raiz quadrada
rc = s ** (1/3) # Raiz cúbica

print("A soma é {}, o produto é {} e a divisão é {:.3f}".format(s, m, d))
print("Divisão inteira {} e potência {}".format(di, e))
print("A soma é {}, a raiz quadrada dele é {:.3f}".format(s, rq), end=" ")
print("Raiz cúbica é {}".format(rc))