import random
numero_secreto = random.randint(1, 10)

while True:
    numero_usuario = int(input("Adivina el numero del 1 al 10: "))
    if numero_usuario == numero_secreto:
        print("Ganaste!")
        break
    else:
        print("Incorrecto, intenta nuevamente!")