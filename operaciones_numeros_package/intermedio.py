from .basico import Basico


class Intermedio(Basico):
    def numeros_n(self, n=0):
        suma = 0
        print('Suma del número 1 al', n)
        for num_indiv in range(1, n+1):
            suma += num_indiv
        print('La suma es igual a:', suma)

    def factorial(self, numero=0):
        print('Número factorial')
        factorial = 1
        if numero != 0:
            for num_indiv in range(1, numero+1):
                factorial *= num_indiv
        print('El factorial es:', factorial)

    def fibonacci(self, n=0):
        print('Fibonacci,', n, 'repeticiones')
        print('0')
        for num_indiv in range(n-1):
            num_increm = 0
            incremento = 1
            for _ in range(num_indiv):
                adicion = num_increm + incremento
                num_increm = incremento
                incremento = adicion
            print(incremento)

    def primos_gemelos(self, num1=0, num2=0):
        if num1 != num2:
            a, b = 0, 0
            if num1 > num2:  # Intercambio de valores en caso de que
                n3 = num1    # num1 > num2, revertirlo.
                num1 = num2
                num2 = n3
            print('Números primos gemelos del', num1, 'al', num2)
            if num2 > 4:
                for i in range(num1, num2+1):
                    incremento = 2
                    primo = True
                    while primo and incremento < i:
                        if i % incremento == 0: primo = False
                        else: incremento += 1
                    if primo and not a: a = i
                    elif primo and a:
                        b = i
                        if b-a == 2:
                            print(a, 'y', b, 'son números primos gemelos')
                        a = i
            else: print('No hay números primos gemelos.')
        else: print('Ingrese números diferentes.')

    def amigos(self, num1=0, num2=0):  # num=1184 y num2=1210 son amigos.
        if num1 != num2:
            print('Números amigos')
            suma_a, suma_b= 0, 0
            if num1 > num2:
                num3 = num1
                num1 = num2
                num2 = num3
            for cont in range(1, num1+1):
                if num1 % cont == 0: suma_a += cont
            for cont in range(1, num2+1):
                if num2 % cont == 0: suma_b += cont
            if suma_a == suma_b and suma_b == suma_a: print('-> Son números amigos')
            else: print('-> No son números amigos')
        else: print('Ingrese números diferentes.')
