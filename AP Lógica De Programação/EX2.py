print('\nBem-vindo a loja do Gabryel Lima Da Silva')
print('\nEscolha o tamanho de pote desejado ==> (P/M/G)\n')
print( 35 * '_' + 'Tabela de preços'.upper() + 44 * '_')
print(95 * '-')
print( '|' + ' '  'Código' + ' ' '|' + '      ' 'Descrição' + '       ' '|' + ' ' 'Tamanho P (500ml)' + ' ' '|' + ' ' 'Tamanho M (1000ml)' + ' ' '|' + ' ' 'Tamanho G (2000ml)' + ' ' '|')
print( '|' + '   '  'TR' + '   ' '|' + ' ' 'Sabores Tradicionais' + ' ' '|' + '      ' 'R$ 6,00' + '      ' '|' + '      ' 'R$ 10,00' + '      ' '|' + '      ' 'R$ 18,00' + '      ' '|')
print( '|' + '   '  'ES' + '   ' '|' + ' ' 'Sabores Especiais' + '    ' '|' + '      ' 'R$ 7,00' + '      ' '|' + '      ' 'R$ 12,00' + '      ' '|' + '      ' 'R$ 21,00' + '      ' '|')
print( '|' + '   '  'PR' + '   ' '|' + ' ' 'Sabores Premium' + '      ' '|' + '      ' 'R$ 8,00' + '      ' '|' + '      ' 'R$ 14,00' + '      ' '|' + '      ' 'R$ 24,00' + '      ' '|')
print(95 * '-')
'''Primeiramente inicio indicando a tabela de escolha dos items para o usuário, depois dessa apresentação desso e armazeno
cada valor referente a tamanho e código do produto em uma lista.'''
P = ['6.00','7.00','8.00']
M = ['10.00','12.00','18.00']
G = ['8.00','14.00','24.00']
a = 0
'''Utilizo a variável 'a' para armazenar o valor de cada operação solicitada.'''
while True:
    t = input('\nDigite o tamanho do pote: ')
    c = input('Digite o código de sabor: ')
    '''Está primeira primeira parte irá receber os valores de tamanho e código do produto.
    Passando pela verificação, será apresentado o tamanho e valor correspondente do produto, e proseguindo para
    a próxima verificação.'''
    while t != 'P' or 'M' or 'G' and  c != 'TR' or 'ES' or 'PR':
        if t == 'P':
            print('\nTamanho pequeno de 500ml selecionado!')
            break
        elif t == 'M':
            print('\nTamanho medio de 1000ml selecionado!')
            break    
        elif t == 'G':
            print('\nTamanho grande de 2000ml selecionado!')
            break
        if c == 'TR':
            print('\nSabor Tradicional escolhido!')
            break
        elif c == 'ES':
            print('\nSabor Especial escolhido!')
            break    
        elif c == 'PR':
            print('\nSabor Premium escolhido!')
            break
        else:
            print('\nTAMANHO ou CÓDIGO inválido(s)')
            break
    '''Seguindo por outras condiciobais será puxado o valor correspondente a cada escolha possível, consequentemente a variável
    'a' mencionada acima acumulará os valores para a operação seguinte ser solicitada.'''
    if t == 'P' and c == 'TR':
        a = a + float(P[0])
        print('Você solicitou um sorvete sabor Tradicional de R${}'.format(P[0]))
    elif t == 'P' and c == 'ES':
        a = a + float(P[1])
        print('Você solicitou um sorvete sabor Especial de R${}'.format(P[1]))
    elif t == 'P' and c == 'PR':
        a = a + float(P[2])
        print('Você solicitou um sorvete sabor Premium de R${}'.format(P[2]))
    if t == 'M' and c == 'TR':
        a = a + float(M[0])
        print('Você solicitou um sorvete sabor Tradicional de R${}'.format(M[0]))
    elif t == 'M' and c == 'ES':
        a = a + float(M[1])
        print('Você solicitou um sorvete sabor Especial de R${}'.format(M[1]))
    elif t == 'M' and c == 'PR':
        a = a + float(M[2])
        print('Você solicitou um sorvete sabor Premium de R${}'.format(M[2]))
    if t == 'G' and c == 'TR':
        a = a + float(G[0])
        print('Você solicitou um sorvete sabor Tradicional de R${}'.format(G[0]))
    elif t == 'G' and c == 'ES':
        a = a + float(G[1])
        print('Você solicitou um sorvete sabor Especial de R${}'.format(G[1]))
    elif t == 'G' and c == 'PR':
        a = a + float(G[2])
        print('Você solicitou um sorvete sabor Premium de R${}'.format(G[2]))
    '''Terminado com a última verificação, caso seja 'S' será somado o valor do acumulador com as operações
    seguintes. Caso contrário irá finalizar e dar a soma dos valores atribuidos.'''
    v1 = input('\nDeseja pedir mais alguma coisa? (S/N): ')
    if v1 == 'S': 
        continue   
    if v1 == 'N':
        print('O valor total a ser pago é de R$ {}'.format(a))
        break



