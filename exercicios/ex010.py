reais = float(input("Quantos reais você tem na carteira? "))
dolar = reais/3.27
print("Você pode comprar {:.2f} dólares com R${:.2f}".format(dolar, reais))

euro = reais/5.94
print("Você pode comprar {:.2f} euros com R${:.2f}".format(euro, reais))

iene = reais/0.034
print("Você pode comprar {:.2f} ienes com RS{:.2F}".format(iene, reais))
