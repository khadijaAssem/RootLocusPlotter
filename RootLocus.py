# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import matplotlib as plt
import matplotlib.pyplot as plt
import Data
import Calculations
import sympy as sp
from sympy import *
import numpy as np

# import numpy as np

# cnums = np.arange(5) + 1j * np.arange(6,11)
# cnums =

# X = [x.real for x in cnums]
# Y = [x.imag for x in cnums]
# array=[]
# for line in f:
#      line=line.split()
#      if line:
#             line=[complex(i) for i in line]

# creating an empty list
# lst =  []
X = []
Y = []
Poles = []
# number of elemetns as input
# n = int(input("Enter number of elements : "))
# iterating till the range
# for i in range(0, n):
#     ele = complex(input())
#     X.append(ele.real)
#     Y.append(ele.imag)
#     Poles.append(ele)
#
# print(X)
# print(Y)
# # X = [x.real for x in lst]
# # Y = [x.imag for x in lst]

X = [0, -25, -50, -50]
Y = [0, 0, 10, -10]
Poles = [0, -25, -50 - 10j, -50 + 10j]

data = Data.Data.getInstance()
data.setX(X)
data.setY(Y)
data.setPoles(Poles)

calculations = Calculations.Calculations()
sigma = calculations.calculateSigma()
w, z = calculations.findLineEquation()
breakAwayPoint = calculations.fidBreakAwayPoint()
sR, sI = calculations.findintersectionWithImag()
poles = calculations.getPoles()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(w[0], z[0].real, ':b', label='Asymptotic Lines')
plt.plot(w[1], z[1].real, ':b')
plt.title('Graph of root locus')

plt.legend(loc='upper left')
lX = []
for i in range(0, len(poles)):
    if poles[i].imag == 0:
        lX.append(poles[i].real)

lY = np.zeros(len(lX))
plt.plot(lX, lY, color='crimson', lw=3)

plt.scatter(X, Y, color='blue', marker='X')
plt.scatter(breakAwayPoint.real, breakAwayPoint.imag, color='red')
plt.scatter(sR, sI, color='red')

y = np.arange(-90, 90, 0.01)

temp = 1 + (y ** 2 / (sigma - breakAwayPoint) ** 2)
temp = temp * (sigma - breakAwayPoint) ** 2
x = np.sqrt(temp) + sigma

plt.plot(x, y)

h = complex(sigma).real
pole1 = complex(poles[3])
a = ((pole1.real - h) ** 2 - pole1.imag ** 2) ** (1 / 2)
b = ((pole1.real - h) ** 2 - pole1.imag ** 2) ** (1 / 2)
y = np.arange(20, 85, 0.01)
temp = 1 + ((y) ** 2 / b ** 2)
temp = temp * a ** 2
x = -temp ** (1 / 2) + h
plt.plot(x, y, lw=1, color='green')
plt.plot(x, -1 * y, lw=1, color='green')

plt.grid()
plt.show()

# temp = 1+(y**2/sI[0]**2)
# temp = temp * (sigma-breakAwayPoint)**2
# x = np.sqrt(temp)+sigma