numero_usuario = int(input("Ingrese un numero entero positivo: "))

contador = numero_usuario
while contador > 0:
    print(contador)
    contador = contador - 1
    if contador == 0:
        print ("Despegue!")
        break