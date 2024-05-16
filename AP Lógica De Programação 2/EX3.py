
def boas_vindas():
    # Mensagem de boas-vindas
    print("==============================================")
    print("Bem-vindo ao sistema de cobrança da copiadora!")
    print("==============================================")

def tabela():
    # Tabela
    print("\n__Digite o serviço desejado__")
    print("|(DIG - para Digitalização)")
    print("|(ICO - para Impressão Colorida)")
    print("|(IPB - para Impressão Preto e Branco)")
    print("|(FOT - para Fotocópia)")
    print("--")

# Função para escolher o serviço desejado
def escolha_servico():
    while True:
        servico = input("\n>>> ").lower()
        if servico in ['dig', 'ico', 'ipb', 'fot']:
            return servico
        else:
            print("Opção inválida! Por favor, escolha entre DIG, ICO, IPB ou FOT.")

# Função para obter o número de páginas com desconto
def num_paginas():
    while True:
        try:
            num_paginas = int(input(">>> Digite o número de páginas: "))
            if num_paginas < 20:
                return num_paginas
            elif 20 <= num_paginas < 200:
                return int(num_paginas * 0.85) # 15% de desconto
            elif 200 <= num_paginas < 2000:
                return int(num_paginas * 0.80) # 20% de desconto
            elif 2000 <= num_paginas < 20000:
                return int(num_paginas * 0.75) # 25% de desconto
            else:
                print("\nNúmero de páginas excede o máximo permitido (20000).")
                print(36*"§")
        except ValueError:
            print("\nPor favor, digite um número válido de páginas.")

# Função para escolher o serviço adicional
def servico_extra():
    while True:
        servico_adicional = input(">>> Deseja algum serviço adicional? (Digite 1 para encadernação simples, 2 para encadernação de capa dura, 0 para nenhum): ")
        if servico_adicional in ['0', '1', '2']:
            return int(servico_adicional)
        else:
            print("\nOpção inválida! Por favor, escolha entre 0, 1 ou 2.")
            print(36*"§")

def run():
    # Mensagem de boas-vindas
    boas_vindas()
    # Tabela 
    tabela()
    try:
        # Obter o serviço desejado
        servico = escolha_servico()

        # Obter o número de páginas com desconto
        num_pag = num_paginas()

        # Obter o serviço adicional
        servico_adicional = servico_extra()

        # Calcular o valor total a pagar
        if servico == 'dig':
            preco_por_pagina = 1.10
        elif servico == 'ico':
            preco_por_pagina = 1.00
        elif servico == 'ipb':
            preco_por_pagina = 0.40
        else:
            preco_por_pagina = 0.20

        valor_total = (preco_por_pagina * num_pag)

        if servico_adicional == 1:
            valor_total += 15
        elif servico_adicional == 2:
            valor_total += 40

        print(29*"=")
        print(f"\nValor total a pagar: R${valor_total:.2f}\n")

    except Exception as e:
        print("Ocorreu um erro:", e)

def main():
    run()

if __name__ == "__main__":
    main()

    
