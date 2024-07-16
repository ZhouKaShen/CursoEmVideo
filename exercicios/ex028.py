from random import randrange

# # Estrutura condicional composta
# num = int(input("Adivinhe um número: "))
# aleatorio = randrange(0, 5)
# print("Número escolhido pelo usuário: {}".format(num))
# print("Número escolhido pelo computador: {}".format(aleatorio))

# if num == aleatorio:
#     print("Você acertou! \nMEUS PARABÉNS!")
# else:
#     print("Você errou! \nTente novamente!")

# print("Fim do programa!")

# Estrutura condicional simplificada
num = int(input("Adivinhe um número: "))
aleatorio = randrange(0, 5, 1)
print("Número escolhido pelo computador: {}".format(aleatorio))
print("Você acertou! \nPARABÉNS!" if num == aleatorio else "Você errou! \nTENTE NOVAMENTE!")
print("Fim do programa!")