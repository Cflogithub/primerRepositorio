while(True):
    print("1.- opción 1")
    print("2.- opción 2")
    print("3.- opción 3")
    opt = int(input("Ingresa una opción: "))
    if 0 < opt and opt < 4:
        break
    else:
        print("Error")

print(f"elegiste la opción: {opt}")



