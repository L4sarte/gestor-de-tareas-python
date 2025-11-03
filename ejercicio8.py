numero_usuario = int(input("Ingrese un numero: "))

for i in range(1, 11):
    resultado = numero_usuario * i
    resultado = f"{numero_usuario} X {i} : {resultado}" 
    print (resultado)