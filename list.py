# palabras = []
# palabras.append('python')
# palabras.append(5)
# palabras.append(True)
# palabras.append(input('digite un mensaje ¡..')) #agregar valor por consola
# palabras.insert(0, 'ID: 2')#para agrgar valor en posicion definida



# print(f'palabras: {len(palabras)}')
# for item in palabras:
#     print(item)

# palabras[3] = # para agregar dato en posicion especifica

# for item in palabras:
#     respuesta = (input(f' quiere actualizar el valor de: \n s/n'))
#     if respuesta == 's':
#         item = input('ingrese el nuevo valor')


    # print(type(item))
# eliminado = palabras.pop()# eliminar un dato especifico
# print(f'eliminado: {eliminado}')



# print(f'palabras: {len(palabras)}')
# for item in palabras:
#     print(item)

#limpiar lista
# palabras.clear()

# print('por posicion ')
# print(palabras[2])

# print('por indice ')
# for indice in range(len(palabras)):
#     print(indice)
#     print(palabras[indice])
#     print(type(indice))

import os

utilies = []
cantidad = []
# funcion de validacion
def inputInt(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except: 
            print("Valor ingresado no valido")



def agregarutil():
    cantidad.append(inputInt('digite la cantidad del nuevo util:  '))
    utilies.append(input('digite el nuevo util '))
    print(f'su util  a sido guardado ')
    print('')
    os.system("pause")

def listarutiles():

    for n in zip(utilies,cantidad):

        print(f'cantidad: {n[1]}  nombre: {n[0]} ')
    os.system("pause")

def actualizarutil():
    posicion = int(input(f'digite la posicio que desea actualizar, la posicion  maxima es de {len[utilies]}'))
    nuevo = input('digite el nuevo util')
    utilies[posicion-1] = nuevo
    print('su nuevo util a sido actualizado ')
    os.system("pause")

def eliminarutil():
    eliminar = int(input(f' ingrese la posicion del util a eliminar, la posicion  maxima es de {len[utilies]} '))
    utilies.pop(eliminar)
    print('su util a sido eliminado ')
    os.system("pause")
    
    
while True:

    #os.system("cls")#limpiar terminal automaticamente
    menu = ''' 
╔══════════════════════════════════════════════════╗
║                                                  ║
║ _____ ______   _______   ________   ___  ___     ║
║|\   _ \  _   \|\  ___ \ |\   ___  \|\  \|\  \    ║
║\ \  \\\__\ \  \ \   __/|\ \  \\ \  \ \  \\\  \   ║
║ \ \  \\|__| \  \ \  \_|/_\ \  \\ \  \ \  \\\  \  ║
║  \ \  \    \ \  \ \  \_|\ \ \  \\ \  \ \  \\\  \ ║
║   \ \__\    \ \__\ \_______\ \__\\ \__\ \_______\║
║    \|__|     \|__|\|_______|\|__| \|__|\|_______|║
║                                                  ║
║            menu                                  ║
║        1. agregar un util nuevo                  ║
║       2. listar todos los utiles                 ║
║       3. actualizar un util                      ║
║       4. eliminar util                           ║
║       5. salir                                   ║
╚══════════════════════════════════════════════════╝ 
  '''

    print(menu)

    opcion = input('digite una accion a realizar ')
    if opcion == '1':
        agregarutil()
    elif opcion == '2':
        listarutiles()
    elif opcion == '3':
        listarutiles()
        actualizarutil()
    elif opcion == '4':
        eliminarutil()
    elif opcion == '5':
        print('chaooooo!!!!!....')
        break
    else:
        print('opcion no valida')
    