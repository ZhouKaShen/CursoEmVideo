nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("Seu nome em letra maiúscula é {}".format(nome.upper()))
print("Seu nome em letra minúscula é {}".format(nome.lower()))

# total_letras = nome.replace(" ", "")
total_letras = nome.count(" ")
print("Seu nome tem ao todo {} letras".format(len(nome) - total_letras))

nome = nome.split()
# print("Seu primeiro nome é {} e ele tem {} letras".format(nome[0], len(nome[0])))

total_letra = nome.find(" ")
print("Seu primeiro nome é {} e ele tem {} letras".format(nome[0], total_letra))
