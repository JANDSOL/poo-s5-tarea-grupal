class Basico:
    def numeros_n(self, n=0):
        print('Numeros del 1 al', n)
        for num_indiv in range(1, n+1):
            if num_indiv != n: print(str(num_indiv) + ', ' ,end='')
            else: print(str(num_indiv) + '.')

    def multiplo(self, numero=0):
        print('Multiplos de', numero)
        for num_indiv in range(1, numero+1):
            if (num_indiv * numero) % num_indiv == 0:
                if num_indiv != numero: print(str(num_indiv*numero) + ', ' ,end='')
                else: print(str(num_indiv*numero) + '.')

    def divisores_numeros(self, numero=0):
        print('Divisores de', numero)
        for num_indiv in range(1, numero+1):
            if numero % num_indiv == 0:
                if num_indiv != numero: print(str(num_indiv) + ', ' ,end='')
                else: print(str(num_indiv) + '.')

    def primo(self, numero=0):
        primo = False
        print('Número primo')
        if numero >= 2:
            for num_indiv in range(2, numero):
                if numero % num_indiv == 0:
                    # print('-> No es primo')
                    primo = True
                    break
            if not primo: print('-> Es primo')
            else: print('-> No es primo')
        else: print('-> No es primo')

    def perfecto(self, numero=0):
        print('Número perfecto')
        suma_acumulada = 0
        for num_indiv in range(1, numero):
            if numero % num_indiv == 0: suma_acumulada += num_indiv
        if numero == suma_acumulada: print('-> El número es perfecto')
        else: print('-> El número no es perfecto')
