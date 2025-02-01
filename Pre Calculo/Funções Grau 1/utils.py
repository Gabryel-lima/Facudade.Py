def regra_de_tres(a: float, b: float, c: float) -> float:
    """
    Resolve problemas de regra de três simples.

    Se a está para b, assim como c está para x:
    
        a / b = c / x
    
    Então x = (b * c) / a
    
    Args:
        a (float): Primeiro número da proporção.
        b (float): Segundo número da proporção.
        c (float): Número para o qual queremos achar o correspondente.
    
    Returns:
        float: O valor de x.
    """
    if a == 0:
        raise ValueError("O primeiro valor (a) não pode ser zero, pois não há proporção válida.")
    
    return (b * c) / a

# Exemplo 1: Se 10 produtos custam 50 reais, quanto custam 7 produtos?
x = regra_de_tres(10, 50, 7)
print(f"7 produtos custam R$ {x:.2f}")

def regra_de_tres_inversa(a: float, b: float, c: float) -> float:
    """
    Resolve problemas de regra de três inversa.

    Se maior valor reduz o resultado, usamos:

        x = (a * b) / c

    Args:
        a (float): Primeiro número da proporção.
        b (float): Segundo número da proporção.
        c (float): Número para o qual queremos achar o correspondente.
    
    Returns:
        float: O valor de x.
    """
    if c == 0:
        raise ValueError("O terceiro valor (c) não pode ser zero.")
    
    return (a * b) / c

# Exemplo 2: Se 5 trabalhadores fazem o serviço em 10 horas, em quantas horas 8 trabalhadores fazem?
x = regra_de_tres_inversa(5, 10, 8)
print(f"8 trabalhadores fazem o serviço em {x:.2f} horas.")

