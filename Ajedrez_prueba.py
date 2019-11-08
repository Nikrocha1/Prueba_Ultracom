# -- coding:utf8 --
import numpy
import random


class Ajedrez:
    def _init_(self, m, n):
        self.m = m
        self.n = n

    def peon(self, m, n):
        """El peon se mueve en direccion vertical de abajo hacia
         arriba por lo cual se consideran los siquientes casos:"""
        a[m, n] = 8
        if m == 6:
            """Al iniciar una partida el peon tiene la opcion de mover dos casillas, por tanto
            cuando se encuentre en la linea m = 6 aparece esta opcion"""
            a[(m - 1), n] = 1
            a[(m - 2), n] = 1
        elif m > 0:
            """Durante el resto de la partida el peon solo puede moverse una casilla hacia arriba en el tablero"""
            a[(m - 1), n] = 1
        else:
            """Al alcanzar el tope del tablero el peon ya no puede moverse en dirección alguna"""
            a[m, n] = 8

    def torre(self, m, n):
        """Para el caso de la torre solo se tiene en cuenta que esta se puede mover tanto en direccion
         horizontal o vertical a lo largo y ancho del tablero"""
        for i in range(0, 8):
            """Movimiento vertical en el tablero"""
            a[i, n] = 1
        for i in range(0, 8):
            """Movimiento horizontal en el tablero"""
            a[m, i] = 1
        a[m, n] = 8

    def rey(self, m, n):
        """El rey solo puede moverse una casilla en cualquier direccion con lo cual deja los siguientes casos:"""
        if m == 0 and n == 0:
            """Cuando se encuentra en la esquina superior izquierda"""
            a[m, n+1] = 1
            a[m+1, n] = 1
            a[m+1, n+1] = 1
        elif m == 7 and n == 0:
            """Cuando se encuentra en la esquina inferior izquierda"""
            a[m, n + 1] = 1
            a[m - 1, n] = 1
            a[m - 1, n + 1] = 1
        elif m == 0 and n == 7:
            """Cuando se encuentra en la esquina superior derecha"""
            a[m+1, n] = 1
            a[m, n-1] = 1
            a[m + 1, n - 1] = 1
        elif m == 7 and n == 7:
            """Cuando se encuentra en la esquina inferior derecha"""
            a[m, n - 1] = 1
            a[m - 1, n] = 1
            a[m - 1, n - 1] = 1
        elif m == 0 and 0 < n < 7:
            """Cuando se encuentra en el borde superior entre la posicion 0 y 7"""
            for i in range(n - 1, n + 2):
                for j in range(m, m + 2):
                    a[j, i] = 1
        elif m == 7 and 0 < n < 7:
            """Cuando se encuentra en el borde inferior entre la posicion 0 y 7"""
            for i in range(n - 1, n + 2):
                for j in range(m - 1, m + 1):
                    a[j, i] = 1
        elif n == 0 and 0 < m < 7:
            """Cuando se encuentra en el borde izquierdo entre la posicion 0 y 7"""
            for i in range(n, n + 2):
                for j in range(m - 1, m + 2):
                    a[j, i] = 1
        elif n == 7 and 0 < m < 7:
            """Cuando se encuentra en el borde derecho entre la posicion 0 y 7"""
            for i in range(n - 1, n + 1):
                for j in range(m - 1, m + 2):
                    a[j, i] = 1
        else:
            """Para el resto de los casos"""
            for i in range(n - 1, n + 2):
                for j in range(m - 1, m + 2):
                    a[j, i] = 1
        a[m, n] = 8

    def caballo(self, m, n):
        """El caballo por su parte cuenta con casos especiales similares a los de la ficha del rey con la diferencia
        de que se deben adicionar algunos mas por la naturaleza de su movimiento"""
        if m == 0 and n == 0:
            """Cuando se encuentra en la esquina superior izquierda"""
            a[m + 2, n + 1] = 1
            a[m + 1, n + 2] = 1
        elif m == 0 and n == 7:
            """Cuando se encuentra en la esquina superior derecha"""
            a[m + 2, n - 1] = 1
            a[m + 1, n - 2] = 1
        elif m == 7 and n == 0:
            """Cuando se encuentra en la esquina inferior izquierda"""
            a[m - 2, n + 1] = 1
            a[m - 1, n + 2] = 1
        elif m == 7 and n == 7:
            """Cuando se encuentra en la esquina inferior izquierda"""
            a[m - 2, n - 1] = 1
            a[m - 1, n - 2] = 1
        elif m == 0 and n == 1:
            """Cuando se encuentra en m = 0 y n = 1"""
            a[m + 2, n - 1] = 1
            a[m + 2, n + 1] = 1
            a[m + 1, n + 2] = 1
        elif m == 0 and n == 6:
            """Cuando se encuentra en m = 0 y n = 6"""
            a[m + 2, n - 1] = 1
            a[m + 2, n + 1] = 1
            a[m + 1, n - 2] = 1
        elif m == 1 and n == 7:
            """Cuando se encuentra en m = 1 y n = 7"""
            a[m + 1, n - 2] = 1
            a[m + 2, n - 1] = 1
            a[m - 1, n - 2] = 1
        elif m == 1 and n == 0:
            """Cuando se encuentra en m = 1 y n = 0"""
            a[m - 1, n + 2] = 1
            a[m + 1, n + 2] = 1
            a[m + 2, n + 1] = 1
        elif m == 6 and n == 0:
            """Cuando se encuentra en m = 6 y n = 0"""
            a[m - 2, n + 1] = 1
            a[m - 1, n + 2] = 1
            a[m + 1, n + 2] = 1
        elif m == 7 and n == 1:
            """Cuando se encuentra en m = 7 y n = 1"""
            a[m - 2, n + 1] = 1
            a[m - 2, n - 1] = 1
            a[m - 1, n + 2] = 1
        elif m == 7 and n == 6:
            """Cuando se encuentra en m = 7 y n = 6"""
            a[m - 2, n + 1] = 1
            a[m - 2, n - 1] = 1
            a[m - 1, n - 2] = 1
        elif m == 6 and n == 7:
            """Cuando se encuentra en m = 6 y n = 7"""
            a[m - 2, n - 1] = 1
            a[m + 1, n - 2] = 1
            a[m - 1, n - 2] = 1
        elif m == 0 and 1 < n < 6:
            """Cuando se encuentra en m = 0 y en 1 < n < 6"""
            a[m + 2, n - 1] = 1
            a[m + 2, n + 1] = 1
            a[m + 1, n - 2] = 1
            a[m + 1, n + 2] = 1
        elif m == 7 and 1 < n < 6:
            """Cuando se encuentra en m = 7 y en 1 < n < 6"""
            a[m - 2, n - 1] = 1
            a[m - 2, n + 1] = 1
            a[m - 1, n - 2] = 1
            a[m - 1, n + 2] = 1
        elif 1 < m < 6 and n == 0:
            """Cuando se encuentra en 1 < m < 6 y en n = 0"""
            a[m + 2, n + 1] = 1
            a[m - 2, n + 1] = 1
            a[m + 1, n + 2] = 1
            a[m - 1, n + 2] = 1
        elif 1 < m < 6 and n == 7:
            """Cuando se encuentra en 1 < m < 6 y en n = 7"""
            a[m + 2, n - 1] = 1
            a[m - 2, n - 1] = 1
            a[m + 1, n - 2] = 1
            a[m - 1, n - 2] = 1
        else:
            """Cuando se encuentra en la zona entre 2 < m < 5 y 2 < n < 5"""
            a[m + 2, n - 1] = 1
            a[m + 2, n + 1] = 1
            a[m - 2, n - 1] = 1
            a[m - 2, n + 1] = 1
            a[m - 1, n - 2] = 1
            a[m + 1, n - 2] = 1
            a[m + 1, n + 2] = 1
            a[m - 1, n + 2] = 1
        a[m, n] = 8

    def alfil(self, m, n):
        """El alfil solo puede moverse de forma diagonal en el tablero. Debido a esto se debio dividir el tablero
         en sus dos diagonales entre (0,0-7,7) y (7,0-0,7) y los espacios correspondientes que quedan
         prensentando los siquientes casos"""
        if m == n:  # caso de n = m
            """cuando la ficha se encuentre en la diagonal (0,0-7,7)"""
            for i in range(0, 8):
                """Movimiento del alfil en forma de pendiente positiva"""
                a[i, i] = 1
            if 0 < n < 4:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(0, (n * 2 + 1)):
                    a[(n * 2) - i, i] = 1
            else:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(n + m - 7, 8):
                    a[n + m - i, i] = 1
        elif m + n == 7:
            """cuando la ficha se encuentre en la diagonal (7,0-0,7)"""
            for i in range(0, 8):
                """Movimiento del alfil en forma de pendiente positiva"""
                a[i, 7 - i] = 1
            if m > n:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(m - n, 8):
                    a[i, i - (m - n)] = 1
            else:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(n - m, 8):
                    a[i - (n - m), i] = 1
        elif n + m < 7:
            for i in range(0, m + n + 1):
                """Movimiento del alfil en forma de pendiente positiva"""
                a[m + n - i, i] = 1
            if m > n:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(m - n, 8):
                    a[i, i - (m - n)] = 1
            else:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(n - m, 8):
                    a[i - (n - m), i] = 1
        elif n + m > 7:
            for i in range(m + n - 7, 8):
                """Movimiento del alfil en forma de pendiente positiva"""
                a[m + n - i, i] = 1
            if m > n:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(m - n, 8):
                    a[i, i - (m - n)] = 1
            else:
                """Movimiento del alfil en forma de pendiente negativa"""
                for i in range(n - m, 8):
                    a[i - (n - m), i] = 1
        elif n > m:
            for i in range(n - m, 8, -1):
                a[i - m - n, i] = 1
        a[m, n] = 8

    def reina(self, m, n):
        """La reina tiene la capacidad de movimiento de la torre y el alfil en conjunto"""
        Ajedrez.alfil(self, m, n)
        Ajedrez.torre(self, m, n)


if __name__ == '__main__':
    m = random.randrange(0, 7, 1, int)
    n = random.randrange(0, 7, 1, int)
    a = numpy.zeros(shape=(8, 8))
    #Ajedrez.caballo(m, m, n)
    print('PIEZAS \
        1. Peon\
        2. Torre \
        3. Alfil \
        4. Caballo \
        5. Reina \
        6. Rey')
    
    op = input('seleccione una opcion (1-6):')   #esta opcion debe ser del 1 al 6
    pieces = {'1': Ajedrez.peon, '2': Ajedrez.torre, '3': Ajedrez.alfil , '4': Ajedrez.caballo , '5': Ajedrez.reina , '6': Ajedrez.rey }
    pieces[op](m,m,n)
    print(a)