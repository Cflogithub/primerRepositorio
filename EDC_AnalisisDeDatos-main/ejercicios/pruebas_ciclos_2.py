palabra_secreta = "python"
while(True):
    dame_palabra = input("Ingresa la palabra secreta: ")
    if dame_palabra == palabra_secreta:
        break
    print("Palabra secreta: incorrecta")
print("Palabra secreta: correcta")
