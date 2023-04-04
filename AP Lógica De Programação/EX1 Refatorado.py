class Produto:

    def __init__(self):
        self.testa_valores_de_entrada()
    
    def testa_valores_de_entrada(self):
        while True: 
            try:
                valor = input('\nDigite o valor do Produto: ')
                self.valor = float(valor)
                
                quantidade = input('Digite a quantidade do produto: ')
                self.quantidade = int(quantidade)
                break
            
            except ValueError:
                print("\nDigite um valor e quantidade válidos.".upper())
    
    
    def valor_com_frete(self):
        valor_sem_frete = self.valor_sem_frete()   

        if self.quantidade <= 0:
            valor_com_frete = valor_sem_frete

        elif self.quantidade >= 1 and self.quantidade < 11:
            valor_com_frete = valor_sem_frete + 30.00

        elif self.quantidade >= 11 and self.quantidade < 101:
            valor_com_frete = valor_sem_frete + 60.00

        elif self.quantidade >= 101 and self.quantidade < 1001:
            valor_com_frete = valor_sem_frete + 120.00
            
        else:
            valor_com_frete = valor_sem_frete + 240.00
        
        return valor_com_frete

    @property
    def valor_sem_frete(self):
        return self.valor * self.quantidade
    
if __name__ == '__main__':

    print('\nBem-vindo a loja de produtos!')
    print(29 * '*')

    produto = Produto()

    print('\nValor sem frete é de R${:.2f}'.format(produto.valor_sem_frete()))
    print('Valor com frete é de R${:.2f}'.format(produto.valor_com_frete()))
    print('')
    print(29 * '*')
    print('\n')
