import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Diagrama de dispersão

#EX1

""" x=np.array([1,2,3,4]) #Valores de X
y=np.array([179.93,172.10,182.30,179.56]) #Valores de y
a,b,correlacao,p,erro=stats.linregress(x,y) #Dados da reta de regressão
print('Reta de regressão: y=%.2fx+%.2f'% (a,b)) #Apresentação da equação da reta
print('coeficiente de correlação: r=%.2f'% correlacao) #Apresentação do coeficiente de correlação
plt.plot(x,y,'o',label='Dados originais') #Gráfico dos dados originais
f=a*x+b #Reta de regressão para gerar os valores de f
plt.plot(x,f,'r',label='Reta de regressão') #Gráfico da reta de regressão
plt.ylim(170,190) #Definição dos limites do eixo y
plt.legend() #Legenda
plt.show() #Apresentação do gráfico """

#EX2

""" x=np.array([80,90,100,110,120,130]) #Valores de x
y=np.array([1000,1050,1080,1110,1200,1250]) #Valores de y
a,b,correlacao,p,erro=stats.linregress(x,y) #Dados da reta de regressão
print('A equação é: y=%.2fx+%.2f'% (a,b)) #Apresentação da equação da reta
print('coeficiente de correlação: r=%.2f'% correlacao) #Apresentação do coeficiente de correlação
previsao=a*140+b #Previsão para o custo referente a 140 unidades
print('Previsão para 140 unidades: R$ %.2f'% previsao) #Apresentação da previsão para 140 unidades """

#EX3

""" x=np.array([1,2,3,4,5]) #Valores de x
y=np.array([180,192,206,220,254]) #Valores de y
a,b,correlacao,p,erro=stats.linregress(x,y) #Dados da reta de regressão
print('A equação é: y=%.2fx+%.2f'%(a,b)) #Apresentação da equação da reta
previsao=a*6+b #Demanda prevista para o sábado
print('Demanda prevista para sábado: R$ %.2f'% previsao)#Apresentação da demanda prevista
 """
#Interpolação
from scipy.interpolate import *

#EX1

""" x=[1,2,3,4,5] #Valores de x
y=[1,4,9,16,25] #Valores de y
f=interp1d(x,y,kind='cubic') #Obtenção da função interpolação
xi=np.linspace(1,5,100) #Valores de x para o gráfico da função interpoladora
yi=f(xi) #Valores de y para a função interpoladora
plt.plot(x,y,'o') #Gráfico dos dados originais
plt.plot(xi,yi) #Gráfico da função interpoladora
plt.show() #Apresentação do gráfico """

#EX2

""" x=[1,2,3,4,5] #Valores de x
y=[1,4,9,16,25] #Valores de y
f=lagrange(x,y) #Obtenção da função interpolação
print(f) #Apresentação da função interpoladora """

#EX3

""" x=[8,11,13,15,18] #Valores de x
y=[20,25,32,30,27] #Valores de y
f=lagrange(x,y) #Obtenção da função interpolação
print(f) #Apresentação da função interpoladora
 """

#EX4

""" x=[8,11,13,15,18] #Valores de x
y=[20,25,32,30,27] #Valores de y
f=interp1d(x,y,kind='cubic') #Obtenção da função interpolação
xi=np.linspace (7,19,100) #Valores de x para o gráfico da função interpoladora
yi=f(xi) #Valores de y para a função interpoladora
plt.plot(x,y,'o') #Gráfico dos dados originais
plt.plot(xi,yi) #Gráfico da função interpoladora
plt.show() #Apresentação do gráfico """

#SÉRIES DE FOURIER
from sympy import *

""" #EX1 com dois termos

x,f=symbols("x f")
init_printing()
f=x**2
s=fourier_series(f,(x,-pi,pi))
s.truncate(2)

#O respectivo gráfico é obtido com base na seguinte sequência de comandos

x=np.linspace(-np.pi,np.pi,100)
f=x**2
y=-4* np.cos(x)+np.pi**2/3
plt.plot(x,y,x,f)
plt.legend(['Aproximação por Fourier','Função original'],loc=2)
plt.show() """

""" #EX2 com três termos 

x,f=symbols("x f")
init_printing()
f=x**2
s=fourier_series(f,(x,-pi,pi))
s.truncate(3)

x=np.linspace(-np.pi,np.pi,100)
f=x**2
y=-4* np.cos(x)+np.pi**2/3
plt.plot(x,y,x,f)
plt.legend(['Aproximação por Fourier','Função original'],loc=2)
plt.show() """

""" #EX2 com quatro termos 

x,f=symbols("x f")
init_printing()
f=x**2
s=fourier_series(f,(x,-pi,pi))
s.truncate(4)

x=np.linspace(-np.pi,np.pi,100)
f=x**2
y=-4* np.cos(x)+np.pi**2/3
plt.plot(x,y,x,f)
plt.legend(['Aproximação por Fourier','Função original'],loc=2)
plt.show() """

#EX2  Utilização das séries de Fourier com 3 aproximações e a função original em um mesmo gráfico

""" x=np.linspace(-np.pi, np.pi,100)
f=x**2
y2=-4*np.cos(x)+np.pi**2/3
y3=-4*np.cos(x)+np.cos(2*x)+np.pi**2/3
y4=-4*np.cos(x)+np.cos(2*x)-4*np.cos(3*x)/9+np.pi**2/3
plt.plot(x,y2,x,y3,x,y4,x,f)
plt. legend(['2 termos ','3 termos','4 termos','Função original'], loc=2)
plt. show() """

#FORMULAÇÃO DE PROBLEMAS DE PROGRAMAÇÃO LINEAR

#EX1

""" Uma indústria de equipamentos de mergulho produz dois tipos de
nadadeiras de borracha. Uma mais curta para uso em piscinas e outra mais
longa para uso em águas abertas. As nadadeiras curtas utilizam 400 gramas
de borracha por par e as nadadeiras longas 700 gramas de borracha para cada
par. A indústria tem uma disponibilidade de 1 tonelada de borracha por mês. O
lucro associado a cada par de nadadeiras curtas é de R$ 50,00 e o lucro para
cada par de nadadeiras longas é de R$ 65,00. Devido a contratos com lojas de
artigos esportivos, a produção mensal mínima de nadadeiras curtas é de 200
pares e a produção mínima de nadadeiras longas é de 100 pares. Sabendo
que o objetivo da indústria é determinar a produção mensal de cada modelo de
nadadeira de modo a maximizar o lucro mensal, formule o problema como um
problema de programação linear.
Resolução:
O primeiro passo é identificarmos as variáveis do problema. Após a
leitura do enunciado, é possível perceber que a indústria deseja maximizar o
lucro e, para isso, pretende decidir quantas nadadeiras de cada modelo deverá
produzir. Como essas quantias ainda não estão definidas, mas a indústria
precisa dessas informações para programar sua produção, as variáveis são:
x1 = quantidade de pares de nadadeiras curtas a serem produzidas
x2 = quantidade de pares de nadadeiras longas a serem produzidas
Já sabemos quais são as variáveis. Agora precisamos obter a função
objetivo. Sabemos que o problema é de maximização. Sabemos também que o
objetivo é maximizar o lucro. Como o lucro referente a cada par de nadadeira
curta é igual a R$ 50,00, e o lucro referente a cada par de nadadeira longa é
igual a R$ 65,00, para termos o lucro total, precisamos multiplicar o 50,00 pela
quantidade de pares de nadadeiras curtas a serem produzidas, ou seja, 50
vezes x1 e somarmos com a multiplicação de 65 pela quantidade de pares de
nadadeiras longas a serem produzidas, ou seja, 65 vezes x2. Denominando o
lucro de L, a função objetivo é
max L = 50x1 + 65x2
20
Precisamos também das restrições que são as condições ou limitações
do problema. A primeira restrição é a quantidade de matéria-prima. Observe
que cada par de nadadeiras curtas requer 400 g de borracha e que cada par de
nadadeiras longas requer 700 g de borracha e que o total de borracha
disponível corresponde a 1 tonelada. Transformando gramas em quilos e
tonelada em quilos, temos a restrição
0,4x1 + 0,7x2 ≤ 1000
O termo “≤” é utilizado, pois a indústria tem no máximo 1000 kg de
borracha à disposição.
As outras duas restrições do problema se referem às quantidades
mínimas de cada tipo de nadadeira a serem produzidas. Como a indústria
precisa produzir no mínimo 200 pares de nadadeiras curtas, a restrição
correspondente é
x1 ≥ 200
e como a quantidade mínima de pares de nadadeiras longas a serem
produzidos é de 100 unidades, a outra restrição é
x2 ≥ 100
Logo, a formulação do problema é
max L = 50x1 + 65x2
0,4x1 + 0,7x2 ≤ 1000
x1 ≥ 200
x2 ≥ 100
Veremos a seguir como é possível utilizarmos o Python para
resolvermos o problema e sabermos quantas blusas e quantas camisetas
precisam ser produzidas para que o lucro seja o maior possível. """

#RESOLUÇÃO DE PROBLEMAS DE PROGRAMAÇÃO LINEAR
from pulp import *

""" Uma indústria de equipamentos de mergulho produz dois tipos de
nadadeiras de borracha. Uma mais curta para uso em piscinas e outra mais
longa para uso em águas abertas. As nadadeiras curtas utilizam 400 gramas
de borracha por par e as nadadeiras longas 700 gramas de borracha para cada
par. A indústria tem uma disponibilidade de 1 tonelada de borracha por mês. O
lucro associado a cada par de nadadeiras curtas é de R$ 50,00 e o lucro para
cada par de nadadeiras longas é de R$ 65,00. Devido a contratos com lojas de
artigos esportivos, a produção mensal mínima de nadadeiras curtas é de 200
pares e a produção mínima de nadadeiras longas é de 100 pares. Sabendo
que o objetivo da indústria é determinar a produção mensal de cada modelo de
nadadeira de modo a maximizar o lucro mensal, resolva o problema como um
problema de programação linear.
Resolução:
Sabemos que a formulação do problema é:
max L = 50x1 + 65x2
0,4x1 + 0,7x2 ≤ 1000
x1 ≥ 200
x2 ≥ 100
Com base nessa formulação, podemos resolver esse problema
utilizando a biblioteca “PuLP”. O primeiro passo é instalar o pacote “pulp”
executando os seguintes comandos: """

prob = LpProblem('Exemplo1',LpMaximize)#Criação do problema de maximização
#Variáveis:
x1=LpVariable("Pares de Nadadeiras Curtas",0)
x2=LpVariable("Pares de Nadadeiras Longas",0)
#Função Objetivo:
prob += 50*x1 + 65*x2
#Restrições:
prob += 0.4*x1 + 0.7*x2 <= 1000
prob += x1 >= 200
prob += x2 >= 100
prob.solve() #Comando para resolver o problema
#Apresentação da solução do problema
for v in prob.variables():
    print(v.name,"=",v.varValue)
print("Lucro máximo s",value(prob.objective))




