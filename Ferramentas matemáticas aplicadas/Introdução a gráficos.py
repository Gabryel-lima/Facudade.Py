import matplotlib.pyplot as plt
import numpy as np

""" x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[25,16,9,4,1,0,1,4,9,16,25]
plt.plot(x,y)
plt.show() """

#####################################

""" x=np.linspace(-5,5,100)
y=x**2
plt.plot(x,y)
plt.show() """

#####################################

'''Uma empresa que fabrica antenas para TV
digital vende cada unidade por R$ 186,00
O custo para a producao de cada unidade é
de R$ 109,00, e os custos fixos totais
correspondem a R$ 11.200,00 por més?

Escreva a função receita e a função custo.

Faca 0 grafico dessas funcées em um mesmo
sistema de eixos coordenados'''

x1=np.linspace(0,300,100)
y1=186*x1
y2=109*x1+11260
plt.plot(x1,y1)
plt.plot(x1,y2)
plt.show()
