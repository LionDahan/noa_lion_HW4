#Lion Dahan 318873338
#Noa Ben Gigi 318355633
import math

import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy.testing import pytest
from math import log, cos
from math import e
x = sp.symbols('x')

def func(f,num): #return the y of the function
    x = sp.symbols('x')
    f = lambdify(x, f)
    return f(num)


def calculate_derivative(f):#נגזרת
    x = sp.symbols('x')
    my_f1 = sp.diff(f, x)
    return my_f1


def Bisection_Method(method,start_point, end_point, epsi= 0.00001):
    #calculate num of iterations
    y = epsi / (end_point - start_point)
    z= (-1) * math.log(y, math.e)
    k= (z // math.log(2, math.e)) + 1
    #__________________________________
    numOfIterations = 0
    while (abs(end_point - start_point) > epsi and numOfIterations < k):
        numOfIterations += 1
        c = (start_point + end_point) / 2
        if func(method, start_point) * func(method, c) > 0:
            start_point = c
        else:
            end_point = c
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("number of iterations for finding bisection:", k)
    return c


def Newton_Raphson(method, func_tag,start_point, end_point, epsi=0.0001):
    derivative = calculate_derivative(method)
    x0 = (start_point + end_point) / 2
    x1 = x0 - (func(method, x0) / func(derivative, x0))
    numOfIterations = 1
    while (abs(x1 - x0) > epsi and func(method, x1) != 0 and numOfIterations <= 101):
        x0 = x1
        x1 = x0 - (func(method, x0) / func(derivative, x0))
        numOfIterations += 1
    if (numOfIterations >= 100):
        return "This part does not converge"  # לא מתכנס
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("number of iterations for finding bisection:", numOfIterations)
        return x1


def little_ranges(method, start_point, end_point, n):
    derivative = calculate_derivative(method)
    temporary_end = start_point + 0.1
    temporary_end = round(temporary_end, 2)#to numbers after dot
    while round(start_point, 2) < end_point:
        if func(method,start_point) * func(method,temporary_end) <0:#check the range on the method
            if n == 1:
                print("x =",Bisection_Method(method, start_point, temporary_end))
            if n == 2:
                print("x =",Newton_Raphson(method, derivative, start_point, temporary_end))
            if n == 3:
                print("x =",secant_method(method, start_point, temporary_end))
        if func(method, temporary_end) == 0.0:
            # check the range on the derivative
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Bisection that only touch:")
            print("x =", temporary_end)
            start_point += 0.1
            start_point = round(start_point, 2)
            temporary_end += 0.1
            temporary_end = round(temporary_end, 2)

        start_point += 0.1
        start_point = round(start_point, 2)
        temporary_end += 0.1
        temporary_end = round(temporary_end, 2)

def secant_method(method, start_point, end_point, epsi=0.0001):
    derivative = calculate_derivative(method)
    x0 = start_point
    x1 = end_point
    numOfIterations = 1
    while (abs(x1 - x0) > epsi and numOfIterations <= 101):
        xr_1 = x0
        x0 = x1
        x1 = (xr_1 * func(method, x0) - x0 * func(method, xr_1)) / (func(method, x0) - func(method, xr_1))
        numOfIterations += 1
    if (numOfIterations >= 100):
        return "This part does not converge"  # לא מתכנס
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("num of iteration for finding bisection:", numOfIterations)
        return x1



def main():
    x = sp.symbols('x')
    k= x**4+x**3-3*x**2
    #k=x**2 -4*x
    start_point=-5
    end_point=5
    print("Hello! Please choose which way do you want to solve your function")
    n= int(input("1= Bisection Method\n2=Newton Raphson\n3=Secant Method"))
    if n==1 or n==2 or n==3:
        little_ranges(k, start_point, end_point, n)
    else:
        print("Error.Choose again.")
        main()



    #f= x**3-x-1
    #secant_method(f, start_point, end_point)





if __name__ == "__main__":
    main()