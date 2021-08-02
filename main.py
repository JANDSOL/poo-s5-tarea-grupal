from os import system as pantalla
from menu_calculadora import CalculadorasMenu
from menu_operacion_numeros import OperacionesConNumeros
from menu_tratamiento_listas import menu as Lista
from menu_operaciones_de_cadenas import menu as OperacionesConCadenas

class MainMenu:
    def __init__(self):
        pass
    
    def seleccionar_menus(self):
        opcion = 0
        NUMERO_OPCIONES = 5
        while opcion != 5:
            pantalla('cls')
            print('MENÚ PRINCIPAL')
            print(' 1) Calculadora')
            print(' 2) Operación Numeros')
            print(' 3) Tratamiento de Listas')
            print(' 4) Operaciones de Cadenas')
            print(' 5) Salir')
            print('--------------------------\n')

            while True:
                try:
                    opcion = int(input('Ingrese una opción entre el 1...[{}]: '.format(NUMERO_OPCIONES)))
                    if opcion > 0 and opcion < 6: break
                    else: print('Ingrese una opción correcta.\n')
                except ValueError: print('Ingrese un valor válido.\n')

            if opcion == 1: CalculadorasMenu().menu()
            elif opcion == 2: OperacionesConNumeros().menu()
            elif opcion == 3: Lista()
            elif opcion == 4: OperacionesConCadenas()

        else:
            print('\n¡Nos vemos pronto!')
            input('Pulsa Enter para salir (enter) <-- ')
            pantalla('cls')


if __name__ == '__main__':
    menu = MainMenu()
    menu.seleccionar_menus()
