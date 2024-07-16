viagem = float(input("Digite a distância da viagem em Km: "))
if viagem <= 200:
    print("Valor a pagar pela viagem: R${:.2f}".format(viagem * 0.50))
else:
    print("Valor a pagar pela viagem longa: R${:.2f}".format(viagem * 0.45))