class Produto:

    def __init__(self,valor,quantidade):
        self.valor = valor
        self.quantidade = quantidade
    
    def testa_valores_de_entrada(self):
        while True: 
            try:
                self.valor = float(self.valor)
                self.quantidade = int(self.quantidade)
                break
            except ValueError:
                print("\nDigite um valor e quantidade válidos.".upper())
                self.valor = input("\nDigite o valor do produto novamente: ")
                self.quantidade = input("Digite a quantidade do produto novamente: ")

    def valor_sem_frete(self):
        return self.valor * self.quantidade
    
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

if __name__ == '__main__':

    print('\nBem-vindo a loja de produtos!')
    print(29 * '*')
    
    valor = input('\nDigite o valor do Produto: ')
    quantidade = input('Digite a quantidade do produto: ')

    produto = Produto(valor,quantidade)
    produto.testa_valores_de_entrada()

    print('\nValor sem frete é de R${:.2f}'.format(produto.valor_sem_frete()))
    print('Valor com frete é de R${:.2f}'.format(produto.valor_com_frete()))
    print('')
    print(29 * '*')
