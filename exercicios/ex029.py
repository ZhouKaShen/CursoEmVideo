velocidade = float(input("Digite a velocidade que andou com o carro: "))
if velocidade >= 80:
    print("Você ultrapassou a velocidade e foi multado!")
    print("Dirija com mais cuidado!")
    print("Valor a pagar: R${}".format(velocidade * 7))

print("Fim do programa!")
