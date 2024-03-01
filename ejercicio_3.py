texto = input("Por favor diligencie su Texto: ")

contador_minusculas = 0
contador_mayusculas = 0

for letra in texto:
    if letra.islower():
        contador_minusculas += 1
    elif letra.isupper():
        contador_mayusculas += 1

print("Minusculas: ", contador_minusculas)
print("Mayusculas:  ", contador_mayusculas)