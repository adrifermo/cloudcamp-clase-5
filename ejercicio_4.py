nombres = []
identificaciones = []

tamaño = 3

for i in range(tamaño):
    print("Igresar el nombre del usuario: ", i + 1)
    nombre = input("Nombre: ")
    identif = input("Identificacion: ")
    
    nombres.append(nombre)
    identificaciones.append(identif)
    
print("Imprimimiendo los datos de los usuarios")

for i in range(len(nombres)):
    print("------")
    print("Nombre: ", nombres[i])
    print("Id", identificaciones[i])
    
