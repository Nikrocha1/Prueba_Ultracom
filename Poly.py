import collections
import itertools

class Poly(object):
    ''' se inicializan las propiedades o atributos del objeto'''
    def __init__(self, *coefp):  
        self.coefp = coefp[::-1]
    
    '''se sobrecargan los metodos especiales''' 
    def __call__(self,x):
        resul = 0
        for index, coef in enumerate(self.coefp):
            resul += coef * (x ** index)
        return resul
       
    def __str__(self):
        '''para imprimir en un formato especifico '''
        num = self.coefp[::1]
        p = ""
        for i in range(len(num)-1,-1,-1):
            if (num[i]>0) and (i==len(num)-1):
                p+= str(num[i])+"x^"+str(i)
            elif (i==0) and (num[i]>0):
                p+= " + "+str(num[i])
            elif (i==0) and (num[i]<0):
                p+= str(num[i])
            elif (num[i]>0):
                p+= "+"+str(num[i])+"x^"+str(i)
            else:
                p += str(num[i])+"x^"+str(i)
        return p
       
    def __add__ (self, coefp2):
        '''realiza la suma de dos polinomios '''
        pol1 = self.coefp
        pol2 = coefp2.coefp
        res = [sum(t) for t in zip(pol1, pol2)]
        return Poly(*res[::-1])
    
    def __sub__ (self, coefp2):
        '''realiza la resta de dos polinomios'''
        pol1 = self.coefp
        pol2 = coefp2.coefp
        res = [t1-t2 for t1,t2 in zip(pol1, pol2)]
        return Poly(*res[::-1])
    
    def __mul__(self, coefp2):
        '''realiza la multiplicacion de dos polinomios tenendo en cuenta los diferentes casos en la prueba'''
        if (isinstance(coefp2, Poly) == True):
            pol1 = self.coefp
            pol2 = coefp2.coefp
            res = [0]*(len(pol1)+len(pol2)-1)
            for pol1pow,pol1co in enumerate(pol1):
                for pol2pow,pol2co in enumerate(pol2):
                    res[pol1pow+pol2pow] += pol1co*pol2co
            
            return Poly(*res[::-1])
        else:
            res = [sca*coefp2 for sca in self.coefp]
            return Poly(*res[::-1])

if __name__ == "__main__":
    x = Poly(3,4,2)
    y = Poly(5,40,8)
    a = x + y
    b = x - y
    z = x * y
    f = y * 8
    print('polinomio 1: '+ str(x))
    print('polinomio 2: '+ str(y))
    print('suma de polinomios: ' + str(a))
    print('resta de polinomios(pol1-pol2): ' + str(b))
    print('multiplicacion de polinomios: ' + str(z)) 
    print('multiplicacion polinomio 2 por 8: ' + str(f))  
    print('eval del polinomio 1(x=5): '+ str(x(5)))

