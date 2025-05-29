lista = [500,3,9,4,7,0,15,80,200,-1,73,7,15,69,72]
num_lista = sorted(lista)
print(f'la lista ordenada es {num_lista}')
print(f'la lista desordenada es {lista}')

lista = [500,3,9,4,7,0,15,80,200,-1,73,7,15,69,72]

def ordenar():
    for izq in range(len(lista)-1):
        for der in range(izq + 1, len(lista)):
            if lista[izq] < lista[der]:
                tem = lista[izq]
                lista[izq] = lista[der]
                lista[der] = tem

        print(f'der:{lista}')
    print(f'izq: {lista}')
ordenar()
print('------------------------------------')

# ordenadad por quicksort con lista determinada
lista = [500,3,9,4,7,0,15,80,200,-1,73,7,15,69,72]

def divisionlist(lista):
    if len(lista) < 1:
        return[]
    
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1 , len(lista)):
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])

    return menores , pivote , mayores

def quicksort(lista):

    if len(lista) < 2:
        return lista
    

    menores , pivote , mayores = divisionlist(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)

print(quicksort(lista))

#ardenar lista de personas mediante sus edades, siendo estas proporcionadas por un usuario

def quicksortlista(lista):
    if len(lista) < 1:
        return lista
    
    pivote = lista[-1] # esta es la ultima posicion
    edadmenores = []
    edadmayores = []

    for i in lista[:-1]: #  indica que da todos los datos excepto el ultimo
        if i['EDAD'] < pivote['EDAD']:
            edadmenores.append(i)
        else:
            edadmayores.append(i)

    return quicksortlista(edadmenores) + [pivote] + quicksortlista(edadmayores)

cantidadRegistro = int(input('digite la cantidad de personas a registrar\n'))
registro=[]

for i in range(cantidadRegistro):
    nombre_persona = input(f'digite el nombre de la persona {i + 1}\n')
    edad_persona = int(input(f'digite la edad de la persona {i + 1}\n'))
    registro.append({'NOMBRE': nombre_persona,  'EDAD':edad_persona})

orden = quicksortlista(registro)

print("\nPersonas ordenadas por edad:")
for i in orden:
    print(f'{i['NOMBRE']} --- {i['EDAD']} años')
    