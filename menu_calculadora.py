from os import system as pantalla
from calculadoras_package.calculadora_estandar import calEstandar
from calculadoras_package.calculadora_cientifica import calCientifica


class CalculadorasMenu:
    def __init__(self):
        pass

    def menu(self):
        pantalla('cls')
        c_cientifica = calCientifica()
        NUMERO_OPCIONES = 10
        opcion = 0

        while opcion != 10:
            print('MENÚ CALCULADORA')
            print('  1) Suma')
            print('  2) Resta')
            print('  3) Multiplicacion')
            print('  4) Division')
            print('  5) Exponente')
            print('  6) Valor Absoluto')
            print('  7) Circunferencia')
            print('  8) Area Circulo')
            print('  9) Area Cuadrado')
            print(' 10) Salir')
            print('-------------------\n')

            while True:  # Validacion de ingreso opcion de menu.
                try:
                    opcion = int(input('Ingrese una opción entre el 1...[{}]: '.format(NUMERO_OPCIONES)))
                    if opcion not in range(1, 11): print('Ingrese una opción disponible.\n')
                    else:
                        print('')
                        break
                except ValueError: print('Ingrese una opción válida.\n')

            if opcion != 10:
                if opcion not in range(6, 10):
                    while True:  # Ingreso para datos, opciones 1 al 5.
                        try:
                            numero1 = float(input('Ingrese un número: '))
                            numero2 = float(input('Ingrese otro número: '))
                            break
                        except ValueError: print('Ingrese valores correctos.\n')
                    print('')
                c_estandar = calEstandar(numero1, numero2)

                if opcion == 1:
                    print('El resultado de esta suma es:', c_estandar.suma())
                elif opcion == 2:
                    print('El resultado de esta resta es:', c_estandar.resta())
                elif opcion == 3:
                    print('El resultado de esta multiplicación es:', c_estandar.multiplicacion())
                elif opcion == 4:
                    print('El resultado de esta división es:', c_estandar.division())
                elif opcion == 5:
                    print('El resultado de {}^{} es: {}'.format(numero1, numero2, c_estandar.exponente()))
                elif opcion == 6:

                    while True:  # Ingreso para datos, opcion 6.
                        try:
                            numero1 = float(input('Ingrese un número: '))
                            break
                        except ValueError:
                            print('Ingrese un valor correcto.\n')

                    print('El valor absoluto es igual a:', c_estandar.valorAbsoluto(numero1))
                else:
                    if opcion in range(7, 9):

                        while True:  # Ingreso de datos, opciones 7 y 8.
                            try:
                                radio = float((input('Ingrese el radio: ')))
                                break
                            except ValueError: print('Ingrese un valor correcto.\n')

                        if opcion == 7:
                            print('El resultado de la circunferencia es:', c_cientifica.circunferencia(radio))
                        else:  # Opcion 8.
                            print('El resultado del área del circulo es:', c_cientifica.areaCirculo(radio))
                    else:  # Opcion 9.

                        while True:  # Ingreso de datos, opcion 9.
                            try:
                                lado = float((input('Ingrese un lado del cuadrado: ')))
                                break
                            except ValueError: print('Ingrese un valor correcto.\n')

                        print('El área del cuadrado es igual a:', c_cientifica.areaCuadrado(lado))

                print('\nLimpiando pantalla...')
                input('Pulsa Enter para continuar (enter) <-- ')
                pantalla('cls')
            else:
                print('¡Nos vemos pronto!')
                input('Pulsa Enter para salir (enter) <-- ')
                pantalla('cls')
