import numpy as np
import sympy as sp
from sympy import *
import cmath
import Data
import math

class Calculations:
    __Poles = []
    __angles = []

    def getPoles(self):
        return self.__Poles
    def __init__(self):
        data = Data.Data.getInstance()
        self.__Poles = data.getPoles()
        print("Poles ",self.__Poles)

    def calculateSigma(self):
        sum = np.sum(self.__Poles)
        self.__sigma = sum/len(self.__Poles)
        print("Sigma equals ",self.__sigma)
        self.calculateAnglesOfAsymptotes()
        return self.__sigma

    def calculateAnglesOfAsymptotes(self):
        size = len(self.__Poles)
        self.__angles = [((2*i+1)*180)/size for i in range (0,size)]
        # for i in range (0,size) :
        #     angle = ((2*i+1)*180)/size
        #     while (angle < -180): angle += 360;
        #     while (angle > 180): angle -= 360;
        #     self.__angles.append(angle)  #lw raga3taha fl function elly ba3daha 5aly l y.append(math.tan(self.__angles[3])*(x[1]- self.__sigma))
        print("Angles are ",self.__angles)
        return self.__angles

    def findLineEquation(self):
        y = []
        x = []
        x.append(np.linspace(-100, 100, 40))
        x.append(np.linspace(-100, 100, 40))
        y.append(math.tan(self.__angles[0]*(math.pi/180))*(x[0]-self.__sigma))
        y.append(math.tan(self.__angles[1]*(math.pi/180))*(x[1]- self.__sigma))
        return x,y

    def fidBreakAwayPoint(self):
        size = len(self.__Poles)
        s,k = symbols('s k')
        self.__expression = 1
        for i in range(0,size):
            self.__expression  *= (s - self.__Poles[i])
        self.__expression += k

        self.__expression = simplify(self.__expression)
        print("Expression is ",self.__expression)
        expr_diff = ((Derivative(self.__expression, s)).doit()).simplify()
        print("Derivative is ",expr_diff)
        solved = solve(expr_diff,s)
        print("Solving derivative we find s = ",solved)

        breakAwayPoint = 0
        for i in range(0,len(solved)):
            solved[i] = complex(solved[i])
            if (np.iscomplex(solved[i])):
                sub = np.angle(complex((s-self.__Poles[0]).subs(s,solved[i])))*(180/math.pi)
                for k in range(1,len(self.__Poles)):
                    ex = complex((s-self.__Poles[k]).subs(s,solved[i]))
                    sub-=(np.angle(complex((s-self.__Poles[k]).subs(s,solved[i])))*(180/math.pi))
                if sub == 180 : breakAwayPoint = solved[i]; break

        print("We choose the break away poit  = ",breakAwayPoint)
        return breakAwayPoint

    def findintersectionWithImag(self):#Routh
        s,k = symbols('s k')
        a = Poly(self.__expression, s)
        coff = a.coeffs()
        rows = len(coff)
        columns = math.ceil(rows / 2)
        routh = []

        for i in range(0,rows):
            routh.append([])
            routh[i%2].append(coff[i])
        routh[1].append(0)

        for row in range(2,rows):
            for column in range(0,len(routh[row-1])-1):
                pivot = routh[row-1][0]
                sub = pivot*routh[row-2][column+1] - routh[row-2][0]*routh[row-1][column+1]
                routh[row].append(sub/pivot)
            routh[row].append(0)

        print("Routh stability criterion table : \n",routh)
        expr = routh[rows-2][0]
        kSolved = solve(expr,k)
        auxillaryEquation = routh[rows-3][0]*(s**2)+routh[rows-3][1].subs(k,kSolved[0])
        print("Auxillary equation equal ",auxillaryEquation)
        sSolved = (solve(auxillaryEquation,s))

        print("S's from auxillary equation are : ",sSolved)
        return [complex(x).real for x in sSolved] , [complex(y).imag for y in sSolved]

    def anglesOfDeparture(self):
        angles = []
        for i in range(0,len(self.__Poles)):
            if np.iscomplex(self.__Poles[i]):
                angle = np.subtract(180,np.sum([(np.angle(self.__Poles[i] - self.__Poles[j]) * (180 / math.pi)) for j in range (0,len(self.__Poles))]))
                while (angle < -360): angle += 360;
                while (angle > 360): angle -= 360;
                angles.append(angle)
        print("Angles ",angles)