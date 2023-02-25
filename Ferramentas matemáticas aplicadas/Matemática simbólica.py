from sympy import *

'''A relação entre o preço de venda x
 de um modelo de aparelho de telefone
 celular e o lucro y referente
 à comercialização desse aparelho é dada
 pela função y=-4x2+4000x-200000
 Sendo assim, qual é o lucro quando o preço
 de venda de cada aparelho corresponde
 a R$ 480,00?

O lucro será de R$ 798.400,00, quando o
 preço unitário for igual a R$ 480,00.
'''
""" x,y = symbols('x y')
y=-4*x**2+4000*x-200000
print(y.subs(x,480)) """

############################################################################################

'''o custo y de produção de x motocicletas é dado pela função
y=0,003x3-0,5x2-50x+5000. Determine o custo referente à produção de 1.100 motocicletas.
'''
""" x,y = symbols('x y')
y=0.003*x**3-0.5*x**2-50*x+5000
print(y.subs(x,1100))"""

############################################################################################

#Função composta

'''Em uma indústria, o custo c referente à
produção diária de x unidades é de
c(x)=x2+2x+300
Sabe-se que o nível de produção dessa
indústria é de x(t) = 20t unidades durante
t horas de trabalho
Expresse o custo de produção em função do
tempo'''

c,x,t = symbols('c x t')
c=x**2+2*x+300
print(c.subs(x,20*t))



