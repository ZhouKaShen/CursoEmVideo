# a = float(input("Primeiro segmento: "))
# b = float(input("Segundo segmento: "))
# c = float(input("Terceiro segmento: "))

# ab = a + b
# ac = a + c
# bc = b + c

# if ab > c and ac > b and bc > a:
#     print("Os segmentos acima PODEM FORMAR um triângulo!")
# else:
#     print("Os segmentos acima NÃO PODEM FORMAR um triângulo!")

print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo Segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos acima PODEM FORMAR triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo")
