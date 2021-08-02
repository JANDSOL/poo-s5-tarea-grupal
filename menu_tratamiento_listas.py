from os import system as pantalla
from operaciones_numeros_package.intermedio import Intermedio


class Lista(Intermedio):
    def __init__(self, lista=[], num=0):
        self.lista = lista
        self.num = num

    def presentar_lista(self):
        print('Recorriendo una lista')
        if len(self.lista) != 0:
            for elemento in range(len(self.lista)):
                if elemento+1 != len(self.lista): print(self.lista[elemento] + ', ', end='')
                else: print(self.lista[elemento] + '.')
        else: print('No hay elemento que recorrer.')

    def buscar_lista(self, valor=''):
        print('Buscar un valor')
        if len(self.lista) != 0:
            ubicacion_del_valor = []
            for posicion, elemento in enumerate(self.lista):
                if elemento == valor: ubicacion_del_valor.append(posicion+1)
            if not not ubicacion_del_valor:  # Entrar solo si hay elementos en lista ubicacion_del_valor.
                print('El valor', valor, 'se encontró en la posición: ', end='')
                for elemento in range(len(ubicacion_del_valor)):  # Recorrer lista ubicacion_del_valor.
                    if elemento+1 != len(ubicacion_del_valor): print(str(ubicacion_del_valor[elemento]) + ', ', end='')
                    else: print(str(ubicacion_del_valor[elemento]) + '.')
            if not ubicacion_del_valor: print('El valor', valor, 'no se encontró en la lista.')
        else: print('No hay valor que buscar porque la lista está vacía.')

    def lista_factorial(self):
        lista_factorial = []
        print('Lista con ', end='')
        Intermedio.factorial(self, self.num)
        for numero_inver in reversed(range(1, self.num+1)):  # reversed revierte el rango de numero.
            lista_factorial.append(numero_inver)
        return lista_factorial

    def primo(self):
        lista_primo = []
        primo = False
        print('Lista de números primos hasta el', self.num)
        for numero in range(self.num+1):
            if numero >= 2:
                for numero_indiv in range(2, numero):
                    if numero % numero_indiv == 0:
                        primo = True
                        break
                if not primo: lista_primo.append(numero)
            else: pass
            primo = False
        return lista_primo

    def lista_notas(self, lista_notas_dict={}):
        print('Lista con notas de alumnos')
        for alumno in lista_notas_dict:
            print(alumno, 'estas son tus notas -> ', end='')
            print('| ', end='')
            for nota in lista_notas_dict[alumno]:
                print(nota, end=' | ')
            print('')

    def insertar_lista(self, posicion=0, valor=0):
        print('Insertar valor en lista según su posición')
        print('Lista antigua ->', self.lista)
        self.lista.insert(posicion-1, valor)
        print('Lista nueva   ->', self.lista)

    def eliminar_lista(self, valor=''):
        print('Eliminar todas las ocurrencias de una lista')
        elementos_repetidos = self.lista.count(valor)
        print('Lista antigua ->', self.lista)
        if elementos_repetidos:
            for _ in range(elementos_repetidos):
                self.lista.remove(valor)
            print('Lista nueva   ->', self.lista)
        else: print('No se encontro ese elemento.')

    def retornar_valor_lista(self, posicion=0):
        print('Retorna cualquier valor de una lista eliminandolo')
        try:
            return self.lista[posicion-1]
        except IndexError:
            print('No existen los suficientes elementos para poder eliminar esa posición de la lista.')
            print('Ingrese otra posición.')

    def copiar_tupla_lista(self, tupla=('Tupla', 'convertida', 'en', 'List@.')):
        print('Copiar tupla a lista\nTupla ya creada...')
        print('Tupla ->', tupla)
        print('Lista ->', list(tupla))

    def vuelto_lista(self, lista_clientes_diccionario={}):
        print('Dar el vuelto a varios clientes')
        for vuelto in lista_clientes_diccionario:
            print('$' + str(vuelto) + ' será entregado a los siguientes clientes -> ', end='')
            print('- ', end='')
            for cliente in lista_clientes_diccionario[vuelto]:
                print(cliente + ' - ', end='')
            print('')


def menu():
    pantalla('cls')
    opcion = 0
    NUMERO_OPCIONES = 11
    while opcion != 11:
        lista = []
        num = 0
        print('MENÚ TRATAMIENTO LISTA')
        print('  1) Recorrer y presentar los datos de una lista')
        print('  2) Buscar un valor en una lista')
        print('  3) Retornar una lista con los factoriales')
        print('  4) Retornar una lista de números primos')
        print('  5) Recorrer una lista de diccionario con notas de alumnos')
        print('  6) Insertar un dato en una Lista dada lo Posición')
        print('  7) Eliminar todas las ocurrencias en una Lista')
        print('  8) Retornar cualquier valor de una lista eliminándolo')
        print('  9) Copiar cada elemento de una tupla en una lista')
        print(' 10) Dar el vuelto a varios clientes')
        print(' 11) Salir')
        print('-----------------------------------------------------------\n')

        while True:
            try:
                opcion = int(input('Ingrese una opción entre el 1...[{}]: '.format(NUMERO_OPCIONES)))
                if opcion in range(1, 12): 
                    print('')
                    break
                else: print('Ingrese una opción disponible.\n')
            except ValueError: print('Ingrese una opción válida.\n')

        if opcion in range(1, 5) or opcion in range(6, 9):  # Opcion 1 2 6 7 8 van a necesitar una lista.
            if opcion not in range(3, 5):
                elemento, valor = '', ''
                print('Ingreso de elementos en una lista')
                print('¡Ingrese salir() para salir del bucle!')
                while elemento.replace(' ', '') != 'salir()':
                    elemento = input('-> Ingrese un elemento: ')
                    if elemento.replace(' ', '') != 'salir()': lista.append(elemento)
                if (opcion == 2 or opcion == 6 or opcion == 7):  # Opcion 2 7 toman adicional un valor.
                    valor = input('-> Ingrese un valor: ')

            if opcion == 3 or opcion == 4 or opcion == 6 or opcion == 8:  # Opcion 3 4 solo necesitaran valores, 6 valor adicional, posicion.
                num = 0
                while True:
                    try:
                        num = int(input('-> Ingrese un número: '))
                        if num > 0: break
                        else: print('Ingrese un número entero mayor a 0.\n')
                    except ValueError:
                        print('Ingrese un valor correcto.\n')

        elif opcion == 5 or opcion == 10:
            nombre, numero, diccionario = '', '', {}
            print('Ingreso de elementos en un diccionario')
            print('¡Ingrese salir() para salir del bucle!')
            if opcion == 5:
                while True:
                    nombre = input('Ingrese un nombre: ')
                    if nombre != 'salir()':
                        diccionario[nombre] = []
                        while True:
                            try:
                                numero = input('Ingrese la calificación: ').replace(' ', '')
                                if numero.replace(' ', '') != 'salir()':
                                    numero_aux = float(numero)
                                    if numero_aux > 0 and numero_aux <= 10:
                                        diccionario[nombre].append(numero_aux)
                                    else: print('Ingrese notas entre 1 al 10.\n')
                                else:
                                    if numero.replace(' ', '') == 'salir()' and not diccionario[nombre]:
                                        print('Ingrese por lo menos un valor.\n')
                                    else: break
                            except ValueError: print('Ingrese un valor correcto.\n')
                    else:
                        if nombre.replace(' ', '') == 'salir()' and not diccionario:
                            print('Ingresa por lo menos un elemento.\n')
                        else: break
                    print('')
            else:
                while True:
                    numero = input('Ingrese el vuelto: $')
                    if numero != 'salir()':
                        try:
                            numero = round(float(numero), 2)
                            diccionario[numero] = []
                            while True:
                                    nombre = input('Ingrese los nombre de los clientes: ').replace(' ', '')
                                    if nombre.replace(' ', '') != 'salir()': diccionario[numero].append(nombre)
                                    else:
                                        if nombre.replace(' ', '') == 'salir()' and not diccionario[numero]:
                                            print('Ingresa al menos un valor.\n')
                                        else: break   
                        except ValueError: print('Ingrese un valor correcto.\n')
                    else:
                        if numero.replace(' ', '') == 'salir()' and not diccionario:
                            print('Ingresa al menos un elemento.\n')
                        else: break
                    print('')

        elif opcion == 9: pass

        obj_lista = Lista(lista, num)
        if opcion != 11:
            print('')
            if opcion == 1:
                obj_lista.presentar_lista()
            elif opcion == 2:
                obj_lista.buscar_lista(valor)
            elif opcion == 3:
                factorial = obj_lista.lista_factorial()
                print('La lista Factorial:', factorial)
            elif opcion == 4:
                primo = obj_lista.primo()
                print(primo)
            elif opcion == 5:
                obj_lista.lista_notas(diccionario)
            elif opcion == 6:
                obj_lista.insertar_lista(num, valor)
            elif opcion == 7:
                obj_lista.eliminar_lista(valor)
            elif opcion == 8:
                lista_valor = obj_lista.retornar_valor_lista(num)
                if lista_valor is not None: print('Elemento de la lista:', lista_valor)
            elif opcion == 9:
                obj_lista.copiar_tupla_lista()
            else:
                obj_lista.vuelto_lista(diccionario)

            print('\nLimpiando pantalla...')
            input('Pulsa Enter para continuar (enter) <-- ')
            pantalla('cls')
        else:
            print('¡Nos vemos pronto!')
            input('Pulsa Enter para salir (enter) <-- ')
            pantalla('cls')
            break
