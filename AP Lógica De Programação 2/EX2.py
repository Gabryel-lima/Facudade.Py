

def main():
    """
    Função principal da interface de cliente para retirada de Açaí e Cupuaçu.

    Essa função implementa as funcionalidades do enunciado, incluindo:
    - Mensagem de boas-vindas com o nome do programador
    - Input do sabor (CP/AC) e mensagem de erro caso inválido
    - Input do tamanho (P/M/G) e mensagem de erro caso inválido
    - Cálculo do valor do pedido com base em sabor e tamanho
    - Acumulador para somar os valores dos pedidos
    - Pergunta ao cliente se deseja pedir mais
    - Utilização das estruturas de controle while, break, continue e if-elif-else
    - Apresentação dos resultados na saída do console

    Argumentos:
        Nenhum.

    Retorno:
        Nenhum.
    """

    # Mensagem de boas-vindas
    print("========================================")
    print("Bem-vindo ao Açaí e Cupuaçu - Retirada!")
    print("========================================")

    # Acumulador de valor total
    valor_total = 0

    # Loop de pedidos
    while True:
        # Input do sabor
        sabor = input("Digite o sabor (CP/AC): ").upper()
        if sabor not in ("CP", "AC"):
            print("Sabor inválido. Tente novamente.")
            continue

        # Input do tamanho
        tamanho = input("Digite o tamanho (P/M/G): ").upper()
        if tamanho not in ("P", "M", "G"):
            print("Tamanho inválido. Tente novamente.")
            continue

        # Cálculo do valor do pedido
        if sabor == "CP":
            if tamanho == "P":
                valor_pedido = 9
            elif tamanho == "M":
                valor_pedido = 14
            else:
                valor_pedido = 18
        else:
            if tamanho == "P":
                valor_pedido = 11
            elif tamanho == "M":
                valor_pedido = 16
            else:
                valor_pedido = 20

        # Acumulador de valor total
        valor_total += valor_pedido

        # Apresentação do pedido
        print(f"\nPedido: {sabor}-{tamanho} - R$ {valor_pedido:.2f}")

        # Pergunta para novo pedido
        nova_compra = input("Deseja pedir mais alguma coisa? (S/N): ").upper()
        if nova_compra != "S":
            break

    # Apresentação do valor total
    print(f"\nValor total dos pedidos: R$ {valor_total:.2f}")

if __name__ == "__main__":
    main()

