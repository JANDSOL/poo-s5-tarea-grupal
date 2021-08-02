from os import system as pantalla
from operaciones_numeros_package.basico import Basico
from operaciones_numeros_package.intermedio import Intermedio


class OperacionesConNumeros:
    def __init__(self):
        pass

    def menu(self):
        pantalla('cls')
        op_basica = Basico()
        op_intermedia = Intermedio()
        opcion = 0
        NUMERO_OPCIONES = 11

        while opcion != 11:
            print('MENÚ OPERACIÓN NÚMEROS')
            print('  1) Presentar los números del 1 al n')
            print('  2) Sumar los números del 1 al n')
            print('  3) Múltiplo de cualquier número')
            print('  4) Presentar los divisores de un número')
            print('  5) Numero Primo')
            print('  6) Factorial de cualquier número')
            print('  7) Fibonacci de una serie de n números')
            print('  8) Perfecto')
            print('  9) Primos gemelos')
            print(' 10) Números amigos')
            print(' 11) Salir')
            print('-----------------------------------------\n')

            while True:  # Validacion de ingreso opcion de menu.
                try:
                    opcion = int(input('Ingrese una opción entre el 1...[{}]: '.format(NUMERO_OPCIONES)))
                    if opcion not in range(1, 12): print('Ingrese una opción disponible.\n')
                    else:
                        print('')
                        break
                except ValueError: print('Ingrese una opción válida.\n')

            if opcion != 11:
                if opcion in range(1, 9):  # Ingreso para datos, opciones 1 al 8.
                    print('De preferencia ingresa números enteros mayor a 0.')
                    while True:
                        try:
                            numero = int(input('Ingrese un número: '))
                            if numero > 0: break
                            else: print('Ingrese un número positivo mayor a 0.\n')
                        except ValueError: print('Ingrese valores correctos.\n')

                else:  # Ingreso para datos, opciones 9 al 10.
                    while True:
                        try:
                            numero1 = int(input('Ingrese un número: '))
                            numero2 = int(input('Ingrese otro número: '))
                            if numero1 > 0 and numero2 > 0: break
                            else: print('Ingrese un número positivo mayor a 0.\n')
                        except ValueError: print('Ingrese valores correctos.\n')
                print('')

                if opcion == 1:
                    op_basica.numeros_n(numero)
                elif opcion == 2:
                    op_intermedia.numeros_n(numero)
                elif opcion == 3:
                    op_intermedia.multiplo(numero)
                elif opcion == 4:
                    op_intermedia.divisores_numeros(numero)
                elif opcion == 5:
                    op_intermedia.primo(numero)
                elif opcion == 6:
                    op_intermedia.factorial(numero)
                elif opcion == 7:
                    op_intermedia.fibonacci(numero)
                elif opcion == 8:
                    op_intermedia.perfecto(numero)
                elif opcion == 9:
                    op_intermedia.primos_gemelos(numero1, numero2)
                else:  # Opcion 10.
                    op_intermedia.amigos(numero1, numero2)

                print('\nLimpiando pantalla...')
                input('Pulsa Enter para continuar (enter) <-- ')
                pantalla('cls')
            # else:  # Opcion 11 para salir.
            #     print('¡Gracias por visitarnos!')
            # input('\nPulsa Enter <-- para salir... ')
            # pantalla('cls')
        else:
            print('¡Nos vemos pronto!')
            input('Pulsa Enter para salir (enter) <-- ')
            pantalla('cls')
