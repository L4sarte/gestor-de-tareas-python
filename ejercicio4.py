numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

operacion = input("Ingrese la operacion que desea realizar(+-*/): ")

if operacion == "+":
    resultado = numero1 + numero2
    print("El resultado de la " + operacion + " es: ", resultado)

elif operacion == "-":

    resultado = numero1-numero2
    print("El resultado de la " + operacion + " es: ", resultado)

elif operacion == "*":

    resultado = numero1 * numero2
    print("El resultado de la " + operacion + " es: ", resultado)

elif operacion == "/":

    resultado = numero1 / numero2
    print("El resultado de la " + operacion + " es: ", resultado)

else:
    print ("Operacion no reconocida")

