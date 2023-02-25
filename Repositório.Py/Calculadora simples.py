print('\nCalculadora')
print('Digite a operação que deseja realizar?(1: Soma, 2: Subtração, 3: Multiplicação ou 4: Divisão)')
print('Ou digite s para sair')

op = (input(':'))
print('Operação selecionada!')

so = '1'
su = '2'
mu = '3'
di = '4'

val1 = float(input('Primeiro valor: '))
val2 = float(input('Segundo valor: '))

while op != 's':
    if op == so:
        print('Seu resultado foi: {}'.format(val1 + val2))
    elif op == su:
        print('Seu resultado foi: {}'.format(val1 - val2))
    elif op == mu:
        print('Seu resultado foi: {}'.format(val1 * val2))
    elif op == di:
        print('Seu resultado foi: {}'.format(val1 / val2))
    else:
        print('Operação inválida!')
    print('Digite a operação que deseja realizar?(1: Soma, 2: Subtração, 3: Multiplicação ou 4: Divisão)')
    op = (input(':'))
    print('Operação selecionada!')
else:
    print('Encerrando o programa!')