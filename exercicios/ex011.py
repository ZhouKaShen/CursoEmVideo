largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))
area = largura * altura
quantidade_pintura = area/2

print("A dimensão da área é de: {}x{}".format(largura, altura))
print("Será necessaria {} Litros de tinta para pintar {}m²".format(quantidade_pintura, area))
