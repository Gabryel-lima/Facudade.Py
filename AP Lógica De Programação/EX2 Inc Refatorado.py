class Sorvetes:

    def __init__(self):
        self.count = 0
        self.valida_tipo()
        self.valida_tamanho()
        self.exibe_o_tipo_e_tamanho()
    
    def exibe_o_tipo_e_tamanho(self):
        print('Você solicitou um sorvete de {}'.format(self.tipos.get(True)))
        print('Tamanho {} de 500ml selecionado!'.format(self.tamanhos.items()))

    def valida_tipo(self): 
        tipos = {1: 'tipo tradicional',
                 2: 'tipo especial', 
                 3: 'tipo premium'}
        
        while True:
            try:
                tipo = int(input('Digite o tipo do pote: '))
                self.tipo = tipo
                self.tipos = tipos

                if self.tipo == 1:
                    for value in tipos.values():
                        return self.exibe_o_tipo_e_tamanho
                            
                elif self.tipo == 2:
                    for value in tipos.values():
                        return self.exibe_o_tipo_e_tamanho

                elif self.tipo == 3:
                    for value in tipos.values():
                        return self.exibe_o_tipo_e_tamanho

            except ValueError:   
                print("\nDigite um tipo válido!!\n".upper())
                

    def valida_tamanho(self):
        tamanhos = {'P': 6.00, 'M': 10.00, 'G': 18.00,
                    'P': 7.00, 'M': 12.00, 'G': 21.00, 
                    'P': 8.00, 'M': 14.00, 'G': 24.00}

        while True:
            try:
                tamanho = str(input('Digite o tamanho do sorvete: '.isupper()))
                self.tamanho = tamanho
                self.tamanhos = tamanhos

                if self.tamanho == 'P':
                    for key,value in tamanhos.fromkeys(key,value):
                        return self.exibe_o_tipo_e_tamanho
                
                elif self.tamanho == 'M':
                    for key,value in tamanhos.fromkeys(key,value):
                        return self.exibe_o_tipo_e_tamanho

                elif self.tamanho == 'G':
                    for key,value in tamanhos.fromkeys(key,value):
                        return self.exibe_o_tipo_e_tamanho
    
            except ValueError:
                print("\nDigite um tamanho válido!!".upper())
                
        
            
if __name__ == '__main__':
    
    print('\nBem-vindo a loja')
    print('\nEscolha o tamanho de pote desejado ==> (P/M/G)\n')
    print( 35 * '_' + 'Tabela de preços'.upper() + 44 * '_')
    print(95 * '-')
    print( '|' + ' '  'Tipos'  + ' ' '|' + '      ' 'Descrição' + '       ' '|' + ' ' 'Tamanho P (500ml)' + ' ' '|' + ' ' 'Tamanho M (1000ml)' + ' ' '|' + ' ' 'Tamanho G (2000ml)' + ' ' '|')
    print( '|' + '   '  '1' + '   ' '|' + ' ' 'Sabores Tradicionais' + ' ' '|' + '      ' 'R$ 6,00' + '      ' '|' + '      ' 'R$ 10,00' + '      ' '|' + '      ' 'R$ 18,00' + '      ' '|')
    print( '|' + '   '  '2' + '   ' '|' + ' ' 'Sabores Especiais' + '    ' '|' + '      ' 'R$ 7,00' + '      ' '|' + '      ' 'R$ 12,00' + '      ' '|' + '      ' 'R$ 21,00' + '      ' '|')
    print( '|' + '   '  '3' + '   ' '|' + ' ' 'Sabores Premium' + '      ' '|' + '      ' 'R$ 8,00' + '      ' '|' + '      ' 'R$ 14,00' + '      ' '|' + '      ' 'R$ 24,00' + '      ' '|')
    print(95 * '-')

    sorvetes = Sorvetes()
