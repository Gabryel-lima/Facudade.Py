import matplotlib.pyplot as plt
import numpy as np

'''A tabela a seguir apresenta os níveis de
 produção de pares de um determinado
 modelo de calçado nos meses de março
a julho'''

""" Mês  Março  Abril  Maio   Junho   Julho
--------------------------------------------
Produção 35.000 29.000 27.000 32.000  33.000 """

'''Por meio do Python, faça um gráfico
relacionando os níveis de produção
com cada um desses meses'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y) 
plt.show() """

#######################################################

'''Agora um formato melhor apresentavel partindo de uma escala arbitrada.'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y)
plt.ylim(0, 40000)
plt.show() """

########################################################

'''Aplicando títulos'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y)
plt.ylim(0,40000)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show() """

########################################################

'''Gafico pontilhado'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y,'r o')
plt.ylim(0,40000)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show() """

########################################################

'''Mesclado com ponto e linha'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y,'b')
plt.plot(x,y,'r o')
plt.ylim(0,40000)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show() """

'''Definindo a espessura da linha'''

""" x=['Março', 'Abril', 'Maio', 'Junho', 'Julho']
y=[35000, 29000, 27000, 32000, 33000]
plt.plot(x,y,'c',linewidth=3)
plt.ylim(0,40000)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show() """

#########################################################

""" x=['Segunda','Terça','Quarta','Quinta','Sexta']
y=[174,197,204,233,252]
plt.plot(x,y,'g')
plt.ylim(0,300)
plt.title('Produção da panificadora')
plt.xlabel('Dia')
plt.ylabel('Produção')
plt.show() """

#########################################################

'''Gráficos de barra'''

""" x=['Março','Abril','Maio','Junho','Julho']
y=[35000,29000,27000,32000,33000]
plt.bar(x,y,0.5)
plt.ylim(0,40000)
plt.title('Produção de calçados de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.show() """ 

#########################################################

'''Gráfico de barra deitado'''

""" x=['Março','Abril','Maio','Junho','Julho']
y=[35000,29000,27000,32000,33000]
plt.barh(x,y,0.5)
plt.title('Produção de calçados de março a julho')
plt.xlabel('Produção')
plt.ylabel('Mês')
plt.show() """

#########################################################

'''Dois gráficos de barra'''

""" mes=['Março','Abril','Maio','Junho','Julho']
x=np.arange(5)
y1=[35000,29000,27000,32000,33000]
y2=[34000,33000,25000,37000,27000]
plt.bar(x,y1,0.3,color='r')
plt.bar(x+0.3,y2,0.3,color='c')
plt.xticks(x,mes)
plt.title('Produção de março a julho')
plt.xlabel('Mês')
plt.ylabel('Produção')
plt.legend(['Prod 1','Prod 2'],loc=1)
plt.show() """

##########################################################

'''Gráficos de pizza'''

""" x=[340,560,290]
cursos=['Computação', 'Elétrica', 'Produção']
plt.axis('equal') #Pra o eixo x e y ter a mesma escala
plt.pie(x,labels=cursos)
plt.title('Número de estudantes por curso')
plt.show() """

'''icrementando a porcentagem'''

""" x=[340,560,290]
cursos=['Computação', 'Elétrica', 'Produção']
plt.axis('equal') #Pra o eixo x e y ter a mesma escala
plt.pie(x,labels=cursos,autopct='%1.1f%%')
plt.title('Número de estudantes por curso')
plt.show() """

############################################################

'''Dando cores e aspecto 3d'''

""" x=[340,560,290]
cursos=['Computação', 'Elétrica', 'Produção']
cores=['r','g','y']
plt.axis('equal') #Pra o eixo x e y ter a mesma escala
plt.pie(x,labels=cursos,colors=cores,shadow=True,autopct='%1.1f%%')
plt.title('Número de estudantes por curso')
plt.show() """

#################################################################

'''Separando setor'''

""" x=[340,560,290]
cursos=['Computação', 'Elétrica', 'Produção']
cores=['r','g','y']
plt.axis('equal') #Pra o eixo x e y ter a mesma escala
plt.pie(x,labels=cursos,colors=cores,shadow=True,explode=(0.1,0,0),autopct='%1.1f%%')
plt.title('Número de estudantes por curso')
plt.show() """

##################################################################

'''Figuras geometricas'''

'''Construa um retângulo verde com base
 igual a 5, altura igual a 7 e canto inferior
 direito no ponto P de coordenadas (2, 1)
'''
import matplotlib.patches as patches

""" fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Rectangle((2, 1), 5, 7, color='green'))
plt.ylim(0,10)
plt.xlim(0,10)
plt.show() """

####################################################################

'''Faça a representação de um
círculo azul com centro em
C(7, 6) e raio igual a 5
'''
""" fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Circle((7,6),5,color='yellow'))
plt.ylim(0,15)
plt.xlim(0,15)
plt.show() """

####################################################################

'''Faça a representação de uma elipse com
centro em C(8, 5) em que o diâmetro
horizontal seja igual a 7, e o vertical seja
igual a 3
'''
""" fig=plt.figure()
fig1=fig.add_subplot(111,aspect='equal')
fig1.add_patch(patches.Ellipse((8,5),7,3,color='orange'))
plt.ylim(0,10)
plt.xlim(0,15)
plt.show() """

#####################################################################

#Criação dos eixos
from mpl_toolkits.mplot3d import *

""" fig=plt.figure()
ax=plt.axes(projection='3d')
plt.show()
 """
######################################################################

#Gráfico de superfície

""" x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(X,Y,Z)
plt.show() """

#######################################################################

#Gráficode linha

""" fig=plt.figure()
ax=plt.axes(projection='3d')
Z=np.linspace(0, 15, 1000)
X=np.sin(Z)
Y=np.cos(Z)
ax.plot3D(X,Y,Z,'red')
plt.show() """

########################################################################

#Superfície aramada

""" x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_wireframe(X,Y,Z)
plt.show() """

#########################################################################

#Curvas de nível

x=np.linspace(-5,5,100)
y=np.linspace(-5,5,100)
X,Y=np.meshgrid(x,y)
Z=X**2+Y**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.contour3D(X,Y,Z,15)
plt.show()


