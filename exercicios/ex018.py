from math import radians, sin, cos, tan

angulo = float(input("Digite um ângulo: "))
angulo_radiano = radians(angulo)
seno = sin(angulo_radiano)
cosseno = cos(angulo_radiano)
tangente = tan(angulo_radiano)

print("O ângulo de {} tem o seno de: {:.2f}".format(angulo, seno))
print("O ângulo de {} tem o cosseno de: {:.2f}".format(angulo, cosseno))
print("O ângulo de {} tem a tangente de: {:.2f}".format(angulo, tangente))
