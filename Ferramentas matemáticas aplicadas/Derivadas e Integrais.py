from sympy import *

""" Calcule, por meio do Python, a derivada primeira
de cada uma das seguintes funções
a) f(x)==2x3-4x2+13x-1 """

""" x,f=symbols("x f")
f=-2*x**3-4*x**2+13*x-1
print(diff(f,x)) """


'''b) g(x)=2x+In(x)'''

""" x,g=symbols("x g")
g=2*x+ln(x)
print(diff(g,x)) """


'''c) h(x) =sen(x)
'''
""" x,h=symbols("x h")
h=sin(x)
print(diff(h,x)) """


""" d) r(x)=tg(x) """

""" x,r=symbols("x r")
r=tan(x)
print(diff(r,x)) """


""" e) q(x) =sen(x)cos(x) """

""" x,q=symbols("x q")
q=sin(x)*cos(x)
print(diff(q,x)) """


""" f) v(x) = raiz(x2 - 5x) """

""" x,v=symbols("x v")
v=(x**2-5*x)**(1/2)
print(diff(v,x)) """


'''t(x)=3x²-4x/2x³+6'''

""" x,t=symbols("x t")
t=(3*x**2-4*x)/(2*x**3+6)
print(diff(t,x)) """


#Derivada segunda

""" Calcule, por meio do Python, a derivada segunda
 de cada uma das seguintes funções """

""" a) f(x)=-2x2-4x3+13x-1 """

""" x,f=symbols("x f")
f=-2*x**3-4*x**2+13*x-1
print(diff(f,x,2)) """



""" b) g(x)=2x+In(x) """
  
""" x,g=symbols("x g")
g=2*x+ln(x)
print(diff(g,x,2)) """



""" c) h(x) =sen(x) """
  
""" x,h=symbols("x h")
h=sin(x)
print(diff(h,x,2)) """
  

#Máximos e Mínimos

'''A relação entre o preço de venda x
 de um modelo de aparelho de telefone
 celular e o lucro y referente
 à comercialização desse aparelho é dada
 pela função y=-4x3+4000x-200000
 Sendo assim, qual é o preço de venda que
 maximiza o lucro?
 Qual é o lucro máximo?
'''

""" x,y = symbols("x y")
y=-4*x**2+4000*x-200000
df=diff(y,x)
d2f=diff(y,x,2)
p=solve(Eq(df,0))
I=y.subs(x,p[0])
ds=d2f.subs(x,p[0])
print('Preço ótimo:',p[0])
print('Lucro máximo:',I)
print('Derivada segunda:',ds) """

###################################################

import matplotlib.pyplot as plt
import numpy as np

'''o custo c referente à produção diária de x
unidades de certo item corresponde a
c(x)=x2-20x+300
Qual é o nível de produção que minimiza o
custo?
 Faça o gráfico
'''

""" x,c = symbols("x c")
c=x**2-20*x+300
df=diff(c,x)
d2f=diff(c,x,2)
p=solve(Eq(df,0))
ds=d2f.subs(x,p[0])
print('Produção ótima:',p[0])
print('Derivada segunda:',ds) """

""" x=np.linspace(0,25,100)
c=x**2-20*x+300
plt.plot(x,c)
plt.show() """


#######################################################

'''Uma indústria de carne congelada realizou
 um estudo e chegou à conclusão de que o
lucro mensal L(x) é dado em função do preço
x do quilo da carne congelada, e essa relação
é descrita pela função L(x)=-120x2+4800x
Determine para quais valores de x o lucro
mensal é máximo
'''

""" x,L = symbols("x L")
L=-120*x**2+4800*x
df=diff(L,x)
d2f=diff(L,x,2)
p=solve(Eq(df,0))
ds=d2f.subs(x,p[0])
print('Preço ótimo:',p[0])
print('Derivada segunda:',ds) """

###################################################

""" A função f(x)=-0,04185x4+2,52027x3-
 descreve a variação do consumo de lanches
 em uma praça de alimentação de um centro
 comercial onde x é o horário, das 12 às 22
 horas, e f(x) é o respectivo consumo em
 unidades vendidas
 Em que horário o consumo foi máximo?
 Em qual horário o consumo foi mínimo?
 Faça o gráfico """

""" x,f = symbols("x f")
f=-0.04185*x**4+2.52027*x**3-54.81718*x**2+509.27586*x-1624.86959
df=diff(f,x)
d2f=diff(f,x,2)
p=solve(Eq(df,0))
print(p)
print('Mínimo: ',p[1])
print('Máximo: ',p[2])

x=np.linspace(12,22,100)
f=-0.04185*x**4+2.52027*x**3-54.81718*x**2+509.27586*x-1624.86959
plt.plot(x,f)
plt.show() """

######################################################################

'''Um objeto desloca-se em linha reta, e a
relação entre a distância considerada em
metros do objeto à origem e o tempo em
segundos é dada por s=2t2+3t
Sabendo que a velocidade corresponde à
derivada de S em relação a t, determine a
velocidade do objeto quando t=2 segundos
'''

""" s,t=symbols("s t")
s=2*t**2+3*t
ds=diff(s,t)
v=ds.subs(t,2)
print('Velocidade: %.2f m/s'% v) """

#############################################################
from mpl_toolkits.mplot3d import Axes3D

#Otimização em 3D

'''Dada a função f(x,y)=x2+y2, faça o gráfico e
em seguida obtenha e classifique os pontos
críticos
'''
""" xx=np.linspace(-5,5,100)
yy=np.linspace(-5,5,100)
x,y=np.meshgrid(xx,yy)
z=x**2+y**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z)
plt.show()

x,y,f = symbols("x y f")
f=x**2+y**2
fx=diff(f,x)
fy=diff(f,y)
fxx=diff(f,x,2)
fyy=diff(f,y,2)
fxy=diff(fx,y)
fyx=diff(fy,x)

px=solve(Eq(fx,0))
py=solve(Eq(fy,0))
fxxp=fxx.subs({x:px[0],y:py[0]})
fyyp=fyy.subs({x:px[0],y:py[0]})
fxyp=fxy.subs({x:px[0],y:py[0]})
fyxp=fyx.subs({x:px[0],y:py[0]})
D=fxxp*fyyp-fxyp*fyxp
print('Solução: (%.2f, %.2f)' % (px[0],py[0]))
print('Determinante:',D)
print('Derivada segunda em relação a x:',fxxp) """

##############################################################

'''Considerando a função
f(x,y)=(1-x2)2+100(y-x2)2, faça o gráfico
 e em seguida determine e classifique os
 pontos críticos
'''

""" xx=np.linspace(-5,5,100)
yy=np.linspace(-5,5,100)
x,y=np.meshgrid(xx,yy)
f=(1-x**2)**2+100*(y-x**2)**2
fig=plt.figure()
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,f)
plt.show()

x,y,f = symbols("x y f")
f=(1-x)**2+2*(3-y)**2
fx=diff(f,x)
fy=diff(f,y)
fxx=diff(f,x,2)
fyy=diff(f,y,2)
fxy=diff(fx,y)
fyx=diff(fy,x)

px=solve(Eq(fx,0))
py=solve(Eq(fy,0))
fxxp=fxx.subs({x:px[0],y:py[0]})
fyyp=fyy.subs({x:px[0],y:py[0]})
fxyp=fxy.subs({x:px[0],y:py[0]})
fyxp=fyx.subs({x:px[0],y:py[0]})
D=fxxp*fyyp-fxyp*fyxp
print('Solução: (%.2f,%.2f)' % (px[0],py[0]))
print('Determinante:',D)
print('Derivada segunda em relação a x:',fxxp) """

################################################################

#Integrais

'''Calcule, por meio do Python, se possível, a integral
 indefinida de cada uma das seguintes funções
a) f(x)==2x3-4x2+13x-1
'''
""" x,f=symbols("x f")
f=-2*x**3-4*x**2+13*x-1
print(integrate(f,x)) """


'''b) g(x)=2x+In(x)
'''
""" x,g=symbols("x g")
g=2*x+ln(x)
print(integrate(g,x)) """


""" c) h(x)=sen(x) """

""" x,h=symbols("xh")
h=sin(x)
print(integrate(h,x)) """


""" d) r(x)=tg(x) """

""" x,r=symbols("x r")
r=tan(x)
print(integrate(r,x)) """



'''e) q(x) =sen(x)cos(x)'''

""" x,q=symbols("x q")
q=sin(x)*cos(x)
print(integrate(q,x)) """


'''Utilizando o Python, calcule a integral
definida da função f(x)==2x2-4x4+33-1 no
 intervalo [1, 2]
'''

""" x,f=symbols("x f")
f=-2*x**3-4*x**2+13*x-1
print(integrate(f,(x,1,2))) """

############################################################

#Áreas

""" Seja a função f(x)=x2
Obtenha a área entre o gráfico de f e o eixo x
 no intervalo [0, 2]
 Faça o gráfico """

""" x,f=symbols("x f")
f=x**2
integrate(f,(x,0,2))

x=np.linspace(-1,3,1000)
f=x**2
plt.plot(x,f,color="blue")
plt.axhline(color="blue")
plt.fill_between(x,f,where=[(x>0) and (x<2)for x in x],color='green')
plt.show() """


""" Qual é a área abaixo da curva y=x3, de x=1 a
x=3? """

""" x,f=symbols("x f")
f=x**3
A=integrate(f,(x,1,3))

x=np.linspace(0.5,3.5,1000)
f=x**3
plt.plot(x,f,color="blue")
plt.axhline(color="blue")
plt.fill_between(x,f,where=[(x>1) and
(x<3) for x in x],color="magenta")
print('Área:',A)
plt.show() """



""" Calcule a área limitada pelo gráfico da função
y=-x2+4x+1 e pelo eixo x """

""" x,f=symbols("x f")
f=-x**2+4*x+1
coeff=[-1,4,1]
r=np.roots(coeff)
A=integrate(f,(x,min(r),max(r)))

x=np.linspace(min(r)-0.5,max(r)+0.5,1000)
f=-x**2+4*x+1
plt.plot(x,f,color="blue")
plt.axhline(color="blue")
plt.fill_between(x,f,where=[(x>min(r)) and (x<max(r)) for x in x],color='yellow')
print('Área:',A)
plt.show() """


""" Calcule a área limitada pelos gráficos das
funções y=2x e y=1/x, com x variando de
1 a 4 """

x,f,g=symbols("x f g")
f=2*x
g=1/x
A=integrate((f-g),(x,1,4))

x=np.linspace(0.5,4.5,1000)
f=2*x
g=1/x
plt.plot(x,f,color="blue")
plt.plot(x,g,color="red")
plt.axhline(color="black")
plt.fill_between(x,f,g,where=[(x>1) and (x<4) for x in x],color='magenta')
print('Área:',A)
plt.show()

