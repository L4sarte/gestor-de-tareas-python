edad = int(input("Ingrese su edad: "))

if edad <= 12:
    
    print ("Eres un niño")

elif edad <= 17:
    print ("Eres un adolecente")

elif edad <= 64:
    print("Eres un adulto")

elif edad >= 65:
    print ("Eres un adulto mayor")
else:
    print ("Edad no valida")