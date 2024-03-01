usuarios = []

tamaño = 1

for i in range(tamaño):
    print("Igresar el nombre del usuario: ", i + 1)
    nombre = input("Nombre: ")
    identif = input("Identificacion: ")
    
    usuario = {'nombre': nombre, 'id': identif}
    usuarios.append(usuario)
    
print("Imprimimiendo los datos de los usuarios")

for i in range(len(usuarios)):
    for key, value in usuarios[i].items():
        print('{0}: {1}'.format(key, value))
    