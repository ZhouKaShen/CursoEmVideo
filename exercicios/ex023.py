# numero = int(input("Digite um número de 0 a 9999: "))
# print("Analisando o número {}".format(numero))
# unidade = str(numero + 10000)

# print("Unidade: {}".format(unidade[4:5]))
# print("Dezena: {}".format(unidade[3:4]))
# print("Centena: {}".format(unidade[2:3]))
# print("Milhar: {}".format(unidade[1:2]))

num = int(input("Digite um número de 0 a 9999: "))
print("Analisando o número {}".format(num))

unidade = num % 10 # Resto
dezena = (num // 10) % 10 # Divisão inteira e depois o resto
centena = (num // 100) % 10 # Divisão inteira e depois o resto
milhar = (num // 1000) % 10 # Divisão inteira e depois o resto

print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))
