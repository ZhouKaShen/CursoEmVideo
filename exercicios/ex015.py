dias_locacao = int(input("Digite quantos dias deseja fazer a locação do carro: "))
km_andados = float(input("Digite quantos quilometros foi andado: "))
total_pagar = (60 * dias_locacao) + (0.15 * km_andados)
print("O total a pagar é de: R${:.2f}".format(total_pagar))
