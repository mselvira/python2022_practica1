## Adivina adivinador....
import random
numero_aleatorio = random.randrange(101)
gane = False
print("Tenés 5 intentos para adivinar un entre 0 y 100")
intento = 1
while intento < 6 and not gane:
    numero_ingresado = int(input('Ingresa tu número:'))
    if numero_ingresado == numero_aleatorio:
        print('Ganaste! y necesitaste {} intento/s!!!'.format(intento))
        gane = True
    else:
        print('Mmmm...No...ese número no es...seguí intentando.')
        intento += 1
if not gane:
    print('\nPerdiste :(\nEl número era:{}'.format(numero_aleatorio))   
