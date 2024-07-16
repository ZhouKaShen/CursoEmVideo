"""from math import pow, sqrt

cateto_oposto = float(input("Digite o comprimento do Cateto Oposto: "))
cateto_adjacente = float(input("Digite o comprimento do Cateto Adjacente: "))
cateto_total = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
hipotenusa = sqrt(cateto_total)

print("Comprimento do Cateto Oposto: {:.2f}".format(cateto_oposto))
print("Comprimento do Cateto Adjacente: {:.2f}".format(cateto_adjacente))
print("Comprimento da Hipotenusa: {:.2f}".format(hipotenusa))"""

"""cateto_oposto = float(input("Digite o Comprimento do Cateto Oposto: "))
cateto_adjacente = float(input("Digite o Comprimeno do Cateto Adjacente: "))
hipotenusa = ((cateto_oposto ** 2) + (cateto_adjacente ** 2)) ** (1/2)

# cateto_total = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
# hipotenusa = pow(cateto_total, 1/2)
print("A Hipotenusa vai medir {:.2f}".format(hipotenusa))"""

from math import hypot
cateto_oposto = float(input("Digite o Comprimento do Cateto Oposto: "))
cateto_adjacente = float(input("Digite o Comprimento do Cateto Adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("A Hipotenusa vai medir: {:.2f}".format(hipotenusa))
