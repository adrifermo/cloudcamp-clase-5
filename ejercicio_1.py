#Mensaje de bienvenida
print("¡Hola! Aqui podras realizar sumas")

#Leemos un primer número
numero1 = input("Por favor ingrese el primer valor: ")

#Leemos un segundo número
numero2 = input("Por favor ingrese el segundo valor: ")

# En este punto tanto numero1 y numero2 son string
# Debes entonces convertirlos a números

#numero1 será entero, así que usamos int()
numero1 = int(numero1)

#numero2 será un real, así que usamos float()
numero2 = float(numero2)

if numero1 > numero2:
    print("Número 1 es mayor")
else:
    print("Número 2 es mayor")

# Mostramos el resultado de la suma
print(numero1, "+", numero2, "=", numero1 + numero2)
