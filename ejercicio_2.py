#Leemos un primer número
numero = input("Por favor ingrese el valor: ")
i = int(numero)

while i<6:
    print(i)
    if i == 3:
        break
    i += 1
    