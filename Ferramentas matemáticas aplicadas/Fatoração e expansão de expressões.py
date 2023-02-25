from sympy import *

""" x = symbols("x")
print(factor(x**2+8*x)) """

##########################################

""" x,y = symbols('x y')
print(factor(x*y**3+2*x**2*y**4)) """

##########################################

""" x = symbols('x')
print(factor((x**2-5*x+6)/(x-2))) """

##########################################

""" x,y = symbols('x y')
print(expand(x*(x+y))) """

##########################################

'''Sabemos que o produto notável
 (a+b)2 pode ser
 interpretado
 geometricamente como a
 área
 de um quadrado de lados
 iguais a "a+b"
 Utilizando Python,
 escreva
 a forma expandida de
 (a+b)2'''

""" a,b = symbols('a b')
print(expand((a+b)**2)) """

###########################################

x,y = symbols('x y')
print(expand((x+y)**4))