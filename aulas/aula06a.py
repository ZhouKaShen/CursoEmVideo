# Tipos primitivos: int, float, bool, str

# Int
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro: "))
s = n1 + n2
print(type(s))
print("A soma entre {0} e {1} vale: {2}".format(n1, n2, s))
#print("A soma entre", n1, "e", n2, "vale:", s)
#print(f"A soma entre {n1} e {n2} vale: {s}")

# Float
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro: "))
s = n1 + n2
print(type(s))
print("A soma entre {} e {} vale: {}".format(n1, n2, s))
# print(f"A soma entre {n1} e {n2} vale: {s}")

# String
n1 = str(input("Digite um número: "))
n2 = str(input("Digite outro: "))
s = n1 + n2
print(type(s))
print("Concatenção: {}".format(s))
# print(f"Concatenação: {s}")
# print("Concatenação:", s)

# Bool
n = bool(input("Digite um valor: "))
print(n)