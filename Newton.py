import math
from math import e

def cosh(x):
  return (((e*x) + (e*(-x)))/2)

def sinh(x):
  return (((e*x) - (e*(-x)))/2)

def f(x):
  return (2*math.cosh(x/4))-x

def Df(x):
  return (0.5*math.sinh(x/4))-1

def Newton(x):
  for i in range(1,10):
    xn= x-(f(x)/Df(x))
    print(xn)
    x=xn

Newton(2)


