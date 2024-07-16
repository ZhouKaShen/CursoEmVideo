frase = "Curso em Vídeo Python"

# # Fatiamento
# print(frase[9])
# print(frase[9:13])
# print(frase[9:21])
# print(frase[9:21:2])
# print(frase[:5])
# print(frase[:15])
# print(frase[9::3])
# print(len(frase))

# # Análise
# print(frase.count("o")) # Conta quantas vezes a letra "o" aparece
# print(frase.count("o", 0, 13)) # Conta quantas vezes a letra "o" aparece do 0 ao 13
# print(frase.find("deo")) # Procurar a posição da palavra "deo"
# print(frase.find("Android"))
# print("Curso" in frase) # Não é uma funcionalidade, é um operador, mas da para fazer análise

# # Transformação
# print(frase.replace("Python", "Android")) # Replace(trocar, reposicionar)
# print(frase.upper()) # Upper é um método, transforma minúsculo em maiúsculo
# print(frase.lower()) # Lower é um método, transforma maiúsculo em minúsculo
# print(frase.capitalize()) # Transforma a primeira letra em maiúsculo e o resto em minúsculo
# print(frase.title()) # Analisa quantas palavras tem e transforma as primeiras letras em maiúsculo
# print(frase.strip()) # Remove todos os espaços desnecessários
# print(frase.rstrip()) # Remove todos os espaços desnecessários do lado direito
# print(frase.lstrip()) # Remove todos os espaços desnecessários do lado esquerdo
# print(frase.split()) # Divide a string, tecnicamente, assim, adicionando em uma nova lista cada palavra

# # Junção
# print("-".join(frase)) # Faz a junção das palavras

# Aula 09

# print(frase[:13])
# print(frase[13:])
# print(frase[1:15])
# print(frase[1:15:2])
# print(frase[1::2])
# print(frase[::2])

# print("""Welcome are you new to programming? 
# Then we presume you will be looking for information 
# about why and how to get started with Python. Fortunately 
# an experienced programmer in any programming language
# (whatever it may be) can pick up Python very quickly. 
# It's also easy for beginners to use and learn, so jump in!""")

# print(frase.upper().count("O"))
# print(frase.count("o"))
# print(len(frase))
# nova_frase = "   Curso Em Vídeo Python  "
# print(len(nova_frase.strip()))

# print(frase[0])

# # frase[0] = "J" 

# # Importante!
# frase = frase.replace("Python", "Android") # Fazer *atribuição* para salvar o valor!
# # Seus microelementos são imutáveis, contudo, pode-se atribuir um novo valor no lugar dele
# # Com uma função de transformação de string e faça uma atribuição
# print(frase)

# print(frase.find("Curso"))
# print(frase.find("Vídeo"))
# print(frase.lower().find("vídeo"))

dividido = frase.split()
print(dividido[2][3])