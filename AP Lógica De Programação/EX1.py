print('\nBem-vindo a loja do Gabryel Lima Da Silva')
print(41 * '*')
p = float(input('\nDigite o valor do Produto:'))
q = int(input('Digite a quantidade do produto:'))
'''Primeiramente irá ser armazenado na memória as variáveis 'p' como valor unitário de cada produto, e a variavel
'q' para a quantidade do produto.'''
va1 = 30.00
va2 = 60.00
va3 = 120.00
va4 = 240.00
mult1 = p * q
'''Após esta etapa amarzeno os valores das embalagens nas variáveis, de acordo com a tabela quantidade.
Em seguida defino uma variavel de multiplicação para distribuir os valores de acordo
com a quantidade do produto.'''
if p <= 0 or p < 11:
    print('Valor sem frete é de R$ {}'.format(mult1))
elif p <= 11 or p < 101:
    print('Valor sem frete é de R$ {}'.format(mult1))
elif p <= 101 or p < 1001:
    print('Valor sem frete é de R$ {}'.format(mult1))
elif p >= 1001:
    print('Valor sem frete é de R$ {}'.format(mult1))
'''Agora utilizo as variáveis dentro das condicionais, para realizar a verificação
do valor sem o frete. Abaixo repito a mesma verificação, mas agora constatando o valor fretado, para
exibir ao usuário com e sem frete. '''
if q <= 0 or q < 11:
    print('Valor com frete é de R$ {}  (frete de R$ 30.00)'.format(mult1+va1))
elif q <= 11 or q < 101:
    print('Valor com frete é de R$ {}  (frete de R$ 60.00)'.format(mult1+va2))
elif q <= 101 or q < 1001:
    print('Valor com frete é de R$ {}  (frete de R$ 120.00)'.format(mult1+va3))
elif q >= 1001:
    print('Valor com frete é de R$ {}  (frete de R$ 240.00)'.format(mult1+va4))
else:
    print('Digite um valor válido')
'''Se por fim nenhuma das condições forem atendidas o programa pedirá uma entrada de valores válidos.'''