# nome = str(input("Qual é o seu nome completo? ")).strip().title()
# print("Seu nome tem Silva? {}".format("Silva" in nome))

# In não é um método, é um operador do Python

nome = str(input("Qual é o seu nome completo? ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))
