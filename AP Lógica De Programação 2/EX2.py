
def main():
    """Função principal da interface de cliente para retirada de Açaí e Cupuaçu."""

    # Mensagem de boas-vindas
    print("========================================")
    print("Bem-vindo ao Açaí e Cupuaçu - Retirada!")
    print("========================================")

    # Acumulador de valor total
    valor_total = 0

    # Loop de pedidos
    while True:
        # Input do sabor
        sabor = input("\nDigite o sabor (CP/AC): ").upper()
        if sabor not in ("CP", "AC"):
            print("\nSabor inválido. Tente novamente.")
            print(29*"§")
            continue

        # Input do tamanho
        tamanho = input("Digite o tamanho (P/M/G): ").upper()
        if tamanho not in ("P", "M", "G"):
            print("\nTamanho inválido. Tente novamente.")
            print(29*"§")
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
        print(29*"-")
        print(f"\nPedido: {sabor} - {tamanho} - R$ {valor_pedido:.2f}")
        print(29*"-")

        # Pergunta para novo pedido
        nova_compra = input("\nDeseja pedir mais alguma coisa? (S/N): ").upper()
        if nova_compra in "S":
            print(38*"=")
            continue
        else:
            print(38*"=")
            break

    # Apresentação do valor total
    print(f"\n>>> Valor total dos pedidos: R$ {valor_total:.2f}\n")

if __name__ == "__main__":
    main()

