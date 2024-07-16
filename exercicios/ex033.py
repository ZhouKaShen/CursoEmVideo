a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

"""if a > b > c:
    print("Maior valor: {}".format(a))
    print("Menor valor: {}".format(c))
if b > a > c:
    print("Maior valor: {}".format(b))
    print("Menor valor: {}".format(c))
if c > b > a:
    print("Maior valor: {}".format(c))
    print("Menor valor: {}".format(a))
if b > c > a:
    print("Maior valor: {}".format(b))
    print("Menor valor: {}".format(a))
if a > c > b:
    print("Maior valor: {}".format(a))
    print("Menor valor: {}".format(b))
if c > a > b:
    print("Maior valor: {}".format(c))
    print("Menor valor: {}".format(b))
"""

"""valores = [a, b, c]

print("O menor valor digitado foi:", min(valores))
print("O maior valor digitado foi:", max(valores))"""

# Verificando quem é o menor
menor = a
if b <= a and b <= c:
    menor = b
if c <= a and c <= b:
    menor = c

# Verificando quem é o maior
maior = a
if b >= a and b >= c:
    maior = b
if c >= a and c >= b:
    maior = c

print("O menor valor digitado foi: {}".format(menor))
print("O maior valor digitado foi: {}".format(maior))