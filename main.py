#ingresar una sifra x y vamos a calcular cuantos billetes de 50,20,10 y 5 tenemos que devolverle al usuario
dinero_disponible =[10, 8, 10, 30]

def mostrarDisponible(montos):
    print('disponible')

    print(f'50k: {montos[0]}\n20k: {montos[1]}',
      f'\n10k: {montos[2]}\n5k: {montos[3]}')

def validar_input(denominacion ):
    cantidad = -1
    while True:
        cantidad = int(input('ingrese la cantidad que desee retirar:  '))
        if cantidad % 5_000 != 0:

            print('ingrese un valor valido\n este ATM solo '+
            f'admite valores multiñlos de {denominacion} COP\nenter para continuar..... ')
        else:   
            return cantidad   
        
def validarDenominacionMenor(denominacion):
    can = len(denominacion)
    tem = 0
    for item in denominacion:
        if denominacion[item] > 0:
            if item == 0:
                tem = 50_000
            elif item == 1:
                tem = 20_000
            elif item == 2:
                tem = 10_000
            else:
                tem = 5_000

    return item
denominacion = validarDenominacionMenor(denominacion=dinero_disponible)
print(f' ')
mostrarDisponible(montos=dinero_disponible)



cantidad = validar_input()


can_50 = 0
can_20 = 0
can_10 = 0
can_5 = 0
total = cantidad

while total > 0:


    if total >= 50_000:
        can_50 = can_50 + 1
        total = total - 50_000
        dinero_disponible [0] -= 1
    elif total >= 20_000:  
        can_20 += 1
        total-= 20_000
        dinero_disponible [1] -= 1
    elif total >= 10_000:
        can_10 += 1
        total -= 10_000
        dinero_disponible [2] -= 1
    elif total >= 5_000:
        can_5 += 1
        total -= 5_000
        dinero_disponible[3] -= 1
    else:
        print('no tenemos fondos suficientes :c')
        break

print(f'cantidad de dinero: {cantidad}\n50k: {can_50}\n20k: {can_20}\n10k: {can_10}\n5k: {can_5}')

mostrarDisponible(montos=dinero_disponible)



   