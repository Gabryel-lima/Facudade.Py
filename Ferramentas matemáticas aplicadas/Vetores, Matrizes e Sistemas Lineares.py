import numpy as np
from sympy import *

#VETORES E MATRIZES

'''É possível realizar operações relacionadas a matrizes e vetores de uma
forma bastante simples por meio do Python.'''

""" A=np.array([[113,2,-1],[5,0,20]])
print(A) """

############################################################

'''Suponha que o vetor v armazena os preços de venda, em dólares, de
algumas mercadorias:
v=(35,00; 16,40; 8,49; 15,56)
E, além disso, que cada dólar corresponde a 4 reais. Obtenha um vetor
w que armazena os preços em reais dessas mercadorias.'''

""" v=np.array([[35.00,16.40,8.49,15.56]])
w=4*v
print(w) """

###########################################################

'''Considere o seguinte vetor:
v=(35,00; 16,40; 8,49; 15,56)
Ele armazena os preços de venda, em dólares, de algumas mercadorias,
e o vetor u armazena os respectivos preços de custo, também em dólares:
5
u=(17,80; 10,20; 5,60; 9,99)
Sabendo-se que a margem de contribuição corresponde ao preço de
venda menos o preço de custo, obtenha o vetor m que contém as respectivas
margens de contribuição, em dólares, dessas mercadorias.'''

""" v=np.array([[35.00,16.40,8.49,15.56]])
u=np.array([[17.80,10.20,5.60,9.99]])
m=v-u
print(m) """

###########################################################

'''Em uma instituição de ensino superior, na disciplina de Geometria
Analítica, os alunos matriculados realizaram quatro avaliações. O vetor “notas”
contém as notas obtidas por um dos estudantes e o vetor “pesos” armazena as
porcentagens referentes a cada avaliação, apresentadas na forma decimal. Os
vetores são:
notas=(80, 95, 100, 70)
e
6
pesos=(0,2; 0,2; 0,3; 0,3)
Sabendo-se que a média do estudante corresponde à soma das
multiplicações de cada nota pelos respectivos pesos e que essa média,
matematicamente, é fornecida pelo produto escalar dos vetores “notas” e
“pesos”, determine a referida média.'''

""" notas=np.array([[80,95,100,70]])
pesos=np.array([[0.2,0.2,0.3,0.3]])
media=np.inner(notas,pesos)
print(media) """

##############################################################

'''Considerando os vetores u=(2, 2, -2) e v=(1, 5, 1), obtenha um vetor w
ortogonal aos vetores u e v, ou seja, um vetor w que forma um ângulo de 90°
com o vetor u e um ângulo de 90° com o vetor v.'''

"""u=np.array([[2,2,-2]])
v=np.array([[1,5,1]])
w=np.cross(u,v)
print(w)"""

###############################################################

'''Na confecção de três tamanhos de camisetas de futebol (P, M e G), são
usados distintivos dos clubes nas cores verde e vermelha. O número de
distintivos usados, por tamanho, é dado pela tabela a seguir.
Camiseta P Camiseta M Camiseta G
Verde 3 1 3
Vermelha 6 5 5
O número de camisetas fabricadas, de cada tamanho, nos meses de maio
e junho, é dado pela seguinte tabela.
10
Maio Junho
Camiseta P 100 50
Camiseta M 50 100
Camiseta G 50 50

Nessas condições, obtenha, por meio do uso de matrizes, a tabela que dá
o total de distintivos de cada cor usados em cada um dos meses de maio e junho.
'''
#Existem duas matrizes agora

""" distintivos=np.array([[3,1,3],[6,5,5]])
camisetas=np.array([[100,50],[50,100],[50,50]])
TotalDeDistintivos=np.matmul(distintivos,camisetas)
print(TotalDeDistintivos) """

##############################################################

#Sistemas lineares

'''Um casal foi a uma lanchonete. Marina consumiu um sanduíche e um
refrigerante e pagou R$ 22,00. Leandro consumiu dois sanduíches e um
refrigerante, totalizando R$ 34,00. Com base nessas informações, determine o
preço de cada sanduíche e o preço de cada refrigerante'''

""" A=np.array([[1,1],[2,1]])
b=np.array([[22],[34]])
x=np.linalg.solve(A,b)
print(x) """

################################################################

'''Uma indústria produz dois modelos de tapetes de pele. O primeiro modelo
tem 3 m2 e o segundo modelo tem 4 m2. O total de pele que a indústria possui
corresponde a 1.900 m2. A produção total de tapetes precisa ser de 550
unidades. Quantas unidades de cada modelo devem ser produzidas para que
toda a matéria-prima seja utilizada e a produção total seja atendida?'''

""" A=np.array([[3,4],[1,1]])
b=np.array([[1900],[550]])
x=np.linalg.solve(A,b)
print(x) """

##############################################################

'''Resolva o sistema linear 
3x+4y-2z=8
x-y+42=19
-4x+y+z=0
'''
""" A=np.array([[3,4,-2],[1,-1,4],[-4,1,1]])
b=np.array([[8],[19],[0]])
X=np.linalg.solve(A,b)
print(X) """

#############################################################

#FUNÇÕES TRIGONOMÉTRICAS

'''Como temos a base e a altura da rampa, para obtermos a respectiva
inclinação, vamos utilizar o arco tangente e, no final, converter a solução para
grau.'''

""" inclinacao=np.arctan(40/150)
print(np.rad2deg(inclinacao)) """

############################################################

#NÚMEROS COMPLEXOS

'''Em Python, a unidade imaginária i é representada pela letra j e o número
complexo “z=a+bi” é escrito como “complex(a,b)”. O número complexo “z=2+4j”
corresponde a “z=complex(2, 4)”.
'''

""" z=complex(2,4)
print(z) """

'''O módulo de um número complexo é dado por “abs()”. Para obtermos o
módulo de “z=2+4j”, podemos escrever “abs(z)”, em que “z=complex(2, 4)”'''

###############################################################
'''Também podemos obter o ângulo formado pelo número complexo. A
função é “angle()”. Para obtermos o ângulo de “z=2+4j”, dado por “z=complex(2,
4)”, basta fazermos “np.angle(z,deg=True)”. O parâmetro “deg=True” é utilizado
quando queremos o ângulo em graus.'''

""" z=complex(2,4)
print(np.angle(z,deg=True)) """

'''Para obtermos o ângulo em radianos, vamos escrever apenas
“np.angle(z)”.'''

'''z=complex(2,4)
print(np.angle(z))'''

'''A soma de números complexos é feita mediante o operador “+”.
Para somarmos z1=2+4j e z2=5+6j, temos a figura 24'''

""" z1=complex(2,4)
z2=complex(5,6)
print(z1+z2) """

'''A multiplicação de números complexos também é facilmente obtida
utilizando o operador “*”.
A multiplicação entre z1=2+4j e z2=5+6j resulta em z1*z2=-14+32j.
'''

""" z1=complex(2,4)
z2=complex(5,6)
print(z1*z2) """

'''Já a divisão entre z1=2+4j e z2=5+6j resulta em z1/z2=0,557+0,131j.'''

""" z1=complex(2,4)
z2=complex(5,6)
print(z1/z2) """

#####################################################################

#SISTEMAS LINEARES COM NÚMEROS COMPLEXOS

'''Resolva o seguinte sistema linear:'''

""" (2+3))a+(5j)6=3+7j
(5-1)a+(3+3/16=6-7j """

""" A=np.array([[complex(2,3), complex(0,5)],[complex(5,-1), complex(3,3)]])
b=np.array([[complex(3,7)],[complex(6,-7)]])
print(np.linalg.solve(A,b)) """

############################################################

""" Na forma matricial, temos: """

""" 8+4j  -3-4j  |l1|  100 < 0°
                     =
    -3-4   8-j   |l2|  50 < -150° """

A=np.array([[complex(8,4), complex(-3,-4)],[complex(-3,-4),complex(8,-1)]])
x1=np.cos(np.deg2rad(0))
y1=np.sin(np.deg2rad(0))
x2=np.cos(np.deg2rad(-150))
y2=np.sin(np.deg2rad(-150))
b=np.array([[100*complex(x1,y1)],[50*complex(x2,y2)]])
print(np.linalg.solve(A,b))



































































































































































































































































