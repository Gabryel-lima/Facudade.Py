

def main():
    """
    Função principal do programa de vendas com desconto.

    Essa função implementa as funcionalidades do enunciado, incluindo:
    - Mensagem de boas-vindas com o nome do programador
    - Input do valor unitário e da quantidade do produto
    - Cálculo do desconto conforme a tabela de descontos
    - Cálculo do valor total sem desconto e com desconto
    - Utilização das estruturas de controle if, elif e else
    - Apresentação de mensagens na saída do console

    Argumentos:
        Nenhum.

    Retorno:
        Nenhum.
    """

    # Mensagem de boas-vindas
    print("\n================================")
    print("Bem-vindo a Loja do Gabryel-lima")
    print("================================")

    # Input do valor unitário e da quantidade do produto
    valor_unitario = int(input("\nDigite o valor unitário do produto: R$ "))
    quantidade = int(input("Digite a quantidade do produto: "))

    # Cálculo do valor total sem desconto
    valor_total_sem_desconto = valor_unitario * quantidade

    # Cálculo do desconto
    if valor_total_sem_desconto < 2500:
        desconto = 0
    elif 2500 <= valor_total_sem_desconto < 6000:
        desconto = 4
    elif 6000 <= valor_total_sem_desconto < 10000:
        desconto = 7
    else:
        desconto = 11

    # Cálculo do valor total com desconto
    valor_desconto = valor_total_sem_desconto * (desconto / 100)
    valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

    # Apresentação dos resultados
    print("--------------------------------------------")
    print(f"\nValor total sem desconto: R$ {valor_total_sem_desconto:.2f}")
    print(f"Valor total com {desconto}% de desconto: R$ {valor_total_com_desconto:.2f}\n")

if __name__ == "__main__":
    main()

