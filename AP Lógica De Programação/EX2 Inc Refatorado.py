class Sorvetes:

    tipos = {1: 'tipo tradicional', 2: 'tipo especial', 3: 'tipo premium'}
    tamanhos = {'P': "pequeno", 'M': "medio", 'G': "grande"}
    precos = {
        1: {'P': 6.00, 'M': 10.00, 'G': 18.00},
        2: {'P': 7.00, 'M': 12.00, 'G': 21.00},
        3: {'P': 8.00, 'M': 14.00, 'G': 24.00}
    }

    def __init__(self,tipo,tamanho):
        self.tipo = tipo
        self.tamanho = tamanho 
        self.valida_tipo()
        self.valida_tamanho()
        self.exibe_o_tipo_e_tamanho()

    def exibe_o_tipo_e_tamanho(self):
        print('Você solicitou um sorvete de {}'.format(self.tipos[self.tipo]))
        print('Tamanho {} de 500ml selecionado!'.format(self.tamanho[self.tamanhos]))

    def valida_tipo(self):

        while True:
            try:
                self.tipo = int(self.tipo)
            except ValueError:
                print("\nDigite um tipo válido!!".upper())
                self.tipo = input('\nDigite o tipo do pote: ')
            
            if self.tipo in self.tipos:
                self.exibe_o_tipo_e_tamanho()
                break
            else:
                ValueError("Insira o tipo correspondente!!".upper())
            
    
    def valida_tamanho(self):
        
        while True:
            try:
                self.tamanho = str(self.tamanho).upper()
            except ValueError:
                print("\nDigite um tamanho válido!!".upper())
                self.tamanho = input('\nDigite o tamanho do pote: ')
            
            if self.tamanho in self.tamanhos:
                break
            else:
                ValueError("Insira o tamanho correspondente!!".upper())

            
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

    tipo = input('\nDigite o tipo do pote: ')
    tamanho = input('Digite o tamanho do sorvete: ')

    sorvetes = Sorvetes(tipo,tamanho)