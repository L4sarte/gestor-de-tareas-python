try:
    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))
    operacion = input("Ingrese una operacion (suma, resta, multi, div): ")

    def sumar(a, b):
        resultado = a + b
        return resultado

    def restar(a, b):
        resultado = a - b
        return resultado

    def multiplicar(a, b):
        resultado = a * b
        return resultado

    def dividir(a, b):
        resultado = a / b
        return resultado

    if operacion == "suma":
        resultado = sumar(numero1, numero2)
        print(f"El resultado es: {resultado}")
    elif operacion == "resta":
        resultado = restar(numero1, numero2)
        print(f"El resultado es: {resultado}")
    elif operacion == "multi":
        resultado = multiplicar(numero1, numero2)
        print(f"El resultado es: {resultado}")
    elif operacion == "div":
        resultado = dividir(numero1, numero2)
        print(f"El resultado es: {resultado}")
    else:
        print("La operacion ingresada no es valida")

except ValueError:
    print("Error: Entrada no valida. Debes ingresar un numero")