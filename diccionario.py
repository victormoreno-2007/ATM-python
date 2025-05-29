scord = (['bajo', 0,25], ['aceptables', 26, 50],['sobresaliente',51, 75],['excelente',76 ,90])



def notadefinitiva(nota):
   for i,n in enumerate (scord,start =1):
       if (nota >= n[1] and nota <= n[2]):
            print (f'la nota es: {i} - {n[0]}')
            break

def promedios():
    mensaje = 'NOTAS\n'
    for i, n in enumerate(scord, start= 1):

        nombre, min, max = n

        mensaje += promedionota(posicion= i, nombre= nombre, rango= [min, max]) + '\n'

    return mensaje


def promedionota(posicion: int, nombre: str,rango: list):
    
    return f'{posicion}. {rango[0]} a {rango[1]}  --> {nombre}'


nota = float(input('ingrese el valor de la nota definitiva\n '))

print(promedios())

notadefinitiva(nota)