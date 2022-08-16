# Declaramos una variable de tipo entero
entero = 15
# imprimimos el valor de entero
print(entero)
# verificamos el tipo con el método type()
t = type(entero)
print(t)


enteroM = 255**255
print(enteroM)
print(type(enteroM))


binario = 0b100
hexadecimal = 0x17
octal = 0o720
print(binario)
print(hexadecimal)
print(octal)




decimal = 9.8
print(decimal)
print(type(decimal))



# si los decimales son mas de 16 nueves = 1
decimal = 0.99999999999999999
print(decimal)




import sys
print(sys.float_info.min)
print(sys.float_info.max)




# si asignamos un valor mayor que el max, la variable tomara el valor infinito
maximo = 1.7976931348623157e+308
print(maximo)
maximo_1 = 1.7976931348623157e+309
print(maximo_1)




# Dividir 1/3 debería resultar 0.3 periódico, pero es imposible representarlo
print("{:.2f}".format(1/3))
print("{:.20f}".format(1/3))



# la siguiente operación debería tener como resultado cero
a = 0.1
b = 0.3
print(a+a+a - b)




print("Hola " * 3)




print(10**3)
print(2**2)

# En esta librería también tenemos una función llamada pow() que es equivalente al operador **.
import math
print(math.pow(10, 3))



print(10//3)  
print(10//10)
