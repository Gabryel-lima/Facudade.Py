class Sorvetes:

    tipos = {
        1: 'tipo tradicional',
        2: 'tipo especial', 
        3: 'tipo premium'
    }
    tamanhos = {
        'P': 'pequeno de 500ml',
        'M': 'medio de 1L',
        'G': 'grande de 2L'
    }
    tabelaValores = {
        'P':{1: 6.00, 2: 7.00, 3: 8.00},
        'M':{1: 10.00, 2: 12.00, 3: 14.00},
        'G':{1: 18.00, 2: 21.00, 3: 24.00}
    }

    def __init__(self):
        self.valida_entrada_tipo()
        self.valida_entrada_tamanho()
        self.valida_tipo()
        self.valida_tamanho()
        self.verifica_valor()
        self.exibe_o_tipo_e_tamanho_e_valor()

    def valida_entrada_tipo(self):
        while True:
            try:
                inputTipo = int(input('Digite o tipo do pote: '))
                if inputTipo in self.tipos.keys():      # Verifica se dentro do OBJ tipos existe o valor inserido pelo Usuario
                    self.inputTipo = inputTipo          # Recebe o valor inserido
                    break
                else:
                    print("\nDigite um tipo válido!!\n".upper())    # Retorna quando ocorre o valor int inserido não está presente no OBJ
            except ValueError:
                print("\nDigite um tipo válido!!\n".upper())    # Retorna quando ocorre um ValueError (inputTipo espera reseber um int, mas recebe uma str)
    
    def valida_entrada_tamanho(self):
        while True:
            try:
                inputTamanho = str(input('Digite o tamanho do sorvete: ')).upper()
                if inputTamanho in self.tamanhos.keys():    # Verifica se dentro do OBJ tipos existe o valor inserido pelo Usuario
                    self.inputTamanho = inputTamanho        # Recebe o valor inserido
                    break
                else:
                    print("\nDigite um tamanho válido!!\n".upper())     # Retorna quando ocorre o valor int inserido não está presente no OBJ
            except ValueError:
                print("\nDigite um tamanho válido!!\n".upper())     # Retorna quando ocorre um ValueError (inputTipo espera reseber um int, mas recebe uma str)

    def valida_tipo(self):
        self.tipo = self.tipos[self.inputTipo]

    def valida_tamanho(self):
        self.tamanho = self.tamanhos[self.inputTamanho]

    def verifica_valor(self):
        self.valor = self.tabelaValores[self.inputTamanho][self.inputTipo]
    
    def exibe_o_tipo_e_tamanho_e_valor(self):
        print('\nVocê solicitou um sorvete de {}'.format(self.tipo))
        print('Tamanho {} selecionado!'.format(self.tamanho))
        print('Valor total R$ {} \n'.format(self.valor))
    
if __name__ == '__main__':
    
    print('\nBem-vindo a loja!')
    print( 35 * '_' + 'Tabela de preços'.upper() + 44 * '_')
    print(95 * '-')
    print( '|' + ' '  'Tipos'  + ' ' '|' + '      ' 'Descrição' + '       ' '|' + ' ' 'Tamanho P (500ml)' + ' ' '|' + ' ' 'Tamanho M (1000ml)' + ' ' '|' + ' ' 'Tamanho G (2000ml)' + ' ' '|')
    print( '|' + '   '  '1' + '   ' '|' + ' ' 'Sabores Tradicionais' + ' ' '|' + '      ' 'R$ 6,00' + '      ' '|' + '      ' 'R$ 10,00' + '      ' '|' + '      ' 'R$ 18,00' + '      ' '|')
    print( '|' + '   '  '2' + '   ' '|' + ' ' 'Sabores Especiais' + '    ' '|' + '      ' 'R$ 7,00' + '      ' '|' + '      ' 'R$ 12,00' + '      ' '|' + '      ' 'R$ 21,00' + '      ' '|')
    print( '|' + '   '  '3' + '   ' '|' + ' ' 'Sabores Premium' + '      ' '|' + '      ' 'R$ 8,00' + '      ' '|' + '      ' 'R$ 14,00' + '      ' '|' + '      ' 'R$ 24,00' + '      ' '|')
    print(95 * '-')
    print('Escolha o tamanho de pote desejado ==> (P/M/G)\n')

    sorvetes = Sorvetes() 