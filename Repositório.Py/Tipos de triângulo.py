a = int(input('\nDigite o valor do triângulo a:'))
b = int(input('Digite o valor do triângulo b:'))
c = int(input('Digite o valor do triângulo c:'))

if a and b and c > 0:
    if a == b == c:
        print('Equilátero')
    elif a + b <= c or b + c <= a:
        if a == b != c:
            print('Isóceles')
        if a != b != c:
            print('Escaléno')
    else:
        print('A soma dos dois lados tem que ser menor ou igual ao terceiro')

else:
    print('Impossível formar um triângulo')