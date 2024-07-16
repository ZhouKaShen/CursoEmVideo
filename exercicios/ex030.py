import math

# Número par é divisivel por 2
# Se a soma dos algarismos é divisivel por 3

num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número {} é um número par!".format(num))
else:
    print("O número {} não é um número par!".format(num))
print("Fim do programa!")