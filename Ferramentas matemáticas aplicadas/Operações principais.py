'''Uma resolução simples de desenso técnico'''
Diametro = 40
a = -0.035
b = 0.042

DiametroMinimo = Diametro + a
DiametroMaximo = Diametro + b

print('Diâmetro minimo: ', DiametroMinimo)
print('Diâmetro maximo: ', DiametroMaximo)

'''Mais também posso delimitar as casas depois da virgula
com o EX parecido abaixo!'''

Diametro = 40
a = -0.035
b = 0.042

DiametroMinimo = Diametro + a
DiametroMaximo = Diametro + b

print('Diâmetro minimo: %.2f' % DiametroMinimo)
print('Diâmetro maximo: %.2f' % DiametroMaximo)