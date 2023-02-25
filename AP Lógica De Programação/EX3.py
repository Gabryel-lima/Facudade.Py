def metragem_limpeza():
    print('\nBem-vindo ao Programa de serviços de Limpeza do Gabryel Lima Da Silva')
    print(80 * '*')
    '''Nessa função será averiguada pela triagem e cálculos dos valores com base nas metragens recebidas em 'm'. Passando
    parâmetros ds variáveis calculadas para a função seguinte.'''
    while True: 
        try:
            m = int(input('Digite a metragem da casa: '))
            if m >= 30 and m < 300:
                v = 60 + 0.3 * m 
                print('Valor de: R$ {}'.format(round(v,2)))
                break
            elif m >= 300 and m < 701:
                v = 120 + 0.5 * m
                print('Valor de: R${}'.format(round(v,2)))
                break
            else:
                v = m < 30 or m > 700
                print('\tNão trabalhamos com valores menores que 30m² ou maiores que 700m²'.upper())
                continue
        except:
            print('\tApenas valores numéricos são aceitos!'.upper())
    tipo_limpeza(v,m)
            
def tipo_limpeza(valor,me):
    print(80 * '-')
    '''Agora está função determinará com base em outro cálculo o valor a ser cobrado.'''
    while True:
        print(80 * '°')
        print('\n\t\tEscolha o tipo de limpeza:'.upper())
        print('B - Básica - Indicada para sujeiras semanais ou quinzenais')
        print('C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras')    
        t = input('\nDIGITE AQUI: ')
        print(80 * '-')
        if t == 'B':
            b = 1
            v2 = valor * b
            print('\nVocê selecionou a limpeza Básica!!!')
            print('Valor do serviço: {}'.format(round(v2,2)))
            print(80 * '-')
            print(80 * '°')
            adicional_limpeza(v2,me,b)
            break
        elif t == 'C':
            c = 1.30
            v1 = valor * c
            print('\nVocê selecionou a limpeza Completa!!!')
            print('Valor do serviço: {}'.format(round(v1,2)))
            print(80 * '-')
            print(80 * '°')
            adicional_limpeza(v1,me,c)
            break
        else:
            print('Apenas as opções apresentadas!'.upper())
            continue

def adicional_limpeza(adi,me,ti):
    '''Finalmente está ultima função perguntará e calculará o valor de acordo com os os adicionais solicitados, se assim
    ocorrer. O o programa finalizará...'''
    a = 0.0
    print(' ' * 30 + 'Adicionais' + ' ' * 30 + 'Valor (R$)')
    print('|' + '¨' * 68 + '|' + '¨' * 10 + '|')
    print('|' + ' ' * 2 + '0- Não desejo mais nada (encerrar)' + '_' * 32 + '|' + '_' * 3 + '0,00' + '_' * 3 + '|')
    print('|' + ' ' * 2 + '1- Passar 10 peças de roupas - R$ 10,00' + '_' * 27 + '|' + '_' * 2 + '10,00' + '_' * 3 + '|')
    print('|' + ' ' * 2 + '2- Limpeza de 1 forno/Micro-ondas - R$ 12,00' + '_' * 22 + '|' + '_' * 2 + '12,00' + '_' * 3 + '|')
    print('|' + ' ' * 2 + '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00' + '_' * 22 + '|' + '_' * 2 + '20,00' + '_' * 3 + '|')
    print('|' + '_' * 68 + '|' + '_' * 10 + '|')
    while True:  
        try:
            ad = int(input('\n=> ')) 
            if ad < 0 or ad > 3:
                print('\tApenas valores mostrados na tabela!'.upper())
            elif ad == 1:
                a += 10
                adi += 10
                print('Você selecionou a 1° opção!')
                print('Valor: R$ {}'.format(round(adi,2)))
                print(80 * '-')
            elif ad == 2:
                a += 12
                adi += 12
                print('Você selecionou a 2° opção!')
                print('Valor: R$ {}'.format(round(adi,2)))
                print(80 * '-')
            elif ad == 3:
                a += 20
                adi += 20
                print('Você selecionou a 3° opção!')
                print('Valor: {}'.format(round(adi,2)))
                print(80 * '-')
            if ad == 0:
                print(80 * '-')
                print('\nPedido finalizado!'.upper())
                print('\nTOTAL: R$ {} (Metragem: {}m² * Tipo: {} + Adicional: R$ {} )'.format(adi,me,ti,a))
                print(80 * '-')
                print(80 * '°')
                break
        except:
            print('' * 8 + 'Apenas valores apresentados na tabela!'.upper())
            
'''Logo a iniciar o programa chama a primeira função, vamos subir ao topo do programa...'''
metragem_limpeza()
