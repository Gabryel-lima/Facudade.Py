from sympy import *
import numpy as np

'''Uma empresa que fabrica antenas para TV
digital vende cada unidade por R$ 186,00
O custo para a producao de cada unidade é
de R$ 109,00
Os custos fixos totais correspondem
a R$ 11.200,00 por més
Escreva a funcao receita e a funcao custo
Determine também o ponto de equilibrio'''

""" x,r,c = symbols('x r c')
r=186*x
c=109*x+11200.0
p=solve(Eq(r,c),x)
print(p)
print(r.subs(x,p[0])) """

##################################################

'''Quais sdo as raizes da funcao y=-x3-5x+9x+11?'''

coeff = [-1,-5,9,11]
print(np.roots(coeff))