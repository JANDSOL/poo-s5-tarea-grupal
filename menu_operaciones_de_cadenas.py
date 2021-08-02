from os import system as pantalla


class OperacionesConCadenas:
    def __init__(self, cadena=''):
        self.cadena = cadena
    
    def recorrerCadena(self):
        for caracter in self.cadena:
            print(caracter)
    
    def buscarCaracter(self, buscado=''):
        caracter = self.cadena.find(buscado)
        if caracter > 0:
            print('El caracter [{}] está dentro de la cadena.'.format(buscado))
        else:
            print('El caracter [{}] no está dentro de la cadena.'.format(buscado))

    def listaPosiciones(self, caracter=''):
        lista_posicion = []
        for indiv in range(0, len(self.cadena)):
            if self.cadena[indiv] == caracter: lista_posicion.append(indiv+1)
        return lista_posicion

    def listaPalabras(self):
        while True:
            if len(self.cadena)+1 > 1: break
            else:
                print('Ingrese una palabra válida.\n')
                self.cadena = input('Ingrese una palabra: ').lower().replace(' ', '')
        return list(self.cadena.split())

    def cadenaLista(self):
        print('Ingreso de elementos')
        print('¡Ingrese salir() para salir del bucle!')
        lista_conver = []
        while True:
            caracter_conver = input('Ingrese caracteres: ')
            if caracter_conver.replace(' ', '') == 'salir()': break
            lista_conver.append(caracter_conver)
        conv_cadena = ''.join(lista_conver)
        print('Lista  ->', lista_conver)
        print('Cadena ->', conv_cadena)
    
    def insertarDato(self, buscado, posicion):
        cadena = list(self.cadena)
        cadena.insert(posicion, buscado)
        cadena_conversion = ''.join(cadena)
        print('Cadena nueva ->', cadena_conversion)
    
    def eliminarOcurrencias(self, buscado):
        print('Cadena nueva ->', self.cadena.lower().replace(buscado, ''))

    def retornaValor(self, posicion):
        cadena = list(self.cadena)
        vueltas = 0
        for idx in posicion:
            if vueltas > 0: cadena.pop((idx-1)-vueltas)
            else: cadena.pop(idx-1)
            vueltas += 1
        return ''.join(cadena)
    
    def concatenarCadena(self, dato):
        print('Cadena concatenada ->', self.cadena + dato)


def menu():
    pantalla('cls')
    cadena = ''
    opcion = 0
    NUMERO_OPCIONES = 10
    while opcion != 10:
        print('MENÚ OPERACIONES DE CADENAS')
        print('  1) Recorrer y presentar los datos de una cadena')
        print('  2) Buscar un carácter en una cadena')
        print('  3) Retornar una lista con la posiciones dado un carácter de la cadena')
        print('  4) Retornar una lista con todas las palabras de una cadena')
        print('  5) Retornar una cadena a partir de una lista')
        print('  6) Insertar un dato en una cadena dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una cadena')
        print('  8) Retornar cualquier valor de una cadena eliminándolo ')
        print('  9) Concatenar cadenas')
        print(' 10) Salir')
        print('-----------------------------------------------------------------------\n')

        while True:
            try:
                opcion = int(input('Ingrese una opción entre el 1...[{}]: '.format(NUMERO_OPCIONES)))
                if opcion not in range(1, 11):
                    print('Ingrese un opción disponible.\n')
                else:
                    print('')
                    break
            except ValueError: print('Ingrese una opción válida.\n')

        if opcion != 10:
            if opcion != 5: cadena = input('Ingrese una cadena: ')
            obj_cadena = OperacionesConCadenas(cadena)
            if opcion == 1:
                print('')
                obj_cadena.recorrerCadena()
            elif opcion == 2:
                print('')
                while True:
                    caracter_buscar = input('Ingrese el caracter a buscar: ').lower().replace(' ', '')
                    if len(caracter_buscar) in range(1, 2): break
                    else: print('Ingrese un caracter válido.\n')
                obj_cadena.buscarCaracter(caracter_buscar)
            elif opcion == 3:
                print('')
                while True:
                    caracter_listar = input('Ingrese el caracter a ser listado: ')
                    if len(caracter_listar) in range(1, 2): break
                    else: print('Ingrese un caracter válido.\n')
                lista_caracter_posicion = obj_cadena.listaPosiciones(caracter_listar)
                print('Posiciones encontradas -> {}'.format(lista_caracter_posicion))
            elif opcion == 4:
                print('')
                lista_palabras = obj_cadena.listaPalabras()
                print('Lista palabras -> {}'.format(lista_palabras))
            elif opcion == 5:
                print('')
                obj_cadena.cadenaLista()
            elif opcion == 6:
                print('')
                dato_insertar = input('Ingrese un dato a insertar en la cadena: ')
                while True:
                    try:
                        insertar_posicion = int(input('Del 1 al {} ingrese la posición: '.format(len(cadena))))
                        if insertar_posicion in range(1, len(cadena)+1): break
                        else: print('Ingrese una posición correcta.\n')
                    except ValueError: print('Ingrese un valor correcto.\n')
                obj_cadena.insertarDato(dato_insertar, insertar_posicion)
            elif opcion == 7:
                print('')
                ocurrencias = input('Ingrese los caracteres para eliminarlos: ').lower()
                obj_cadena.eliminarOcurrencias(ocurrencias)
            elif opcion == 8:
                print('')
                print('Ingreso de posiciones')
                print('¡Ingrese salir() para salir del bucle!')
                posiciones = set()
                while True:
                    posicion_indiv = input('Del 1 al {} ingrese las posiciones a eliminar: '.format(len(cadena)))
                    if posicion_indiv.replace(' ', '') == 'salir()': break
                    try:
                        posicion_indiv = int(posicion_indiv)
                        if posicion_indiv in range(1, len(cadena)+1): posiciones.add(posicion_indiv)
                        else: print('Ingrese una posición correcta.\n')
                    except ValueError: print('Ingrese valores válidos.\n')
                valor_n = obj_cadena.retornaValor(posiciones)
                print('Cadena nueva ->', valor_n)
            else:
                print('')
                cadena_concatenar = input('Ingrese otra cadena: ')
                obj_cadena.concatenarCadena(cadena_concatenar)

            print('\nLimpiando pantalla...')
            input('Pulsa Enter para continuar (enter) <-- ')
            pantalla('cls')

        else:
            print('¡Nos vemos pronto!')
            input('Pulsa Enter para salir (enter) <-- ')
            pantalla('cls')
