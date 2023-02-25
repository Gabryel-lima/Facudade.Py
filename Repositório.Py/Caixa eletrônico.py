v = int(input('\nDigite o valor da quantia: '))

while True:

    if v >= 100:
        cedulas100 = v // 100
        v -= cedulas100 * 100
        print('A quantidade notas de 100: {}'.format(cedulas100))
        if not v:
            break
    if v >= 50:
        cedulas50 = v // 50
        v -= cedulas50 * 50
        print('A quantidade notas de 50: {}'.format(cedulas50))
        if not v:
            break
    if v >= 20:
        cedulas20 = v // 20
        v -= cedulas20 * 20
        print('A quantidade notas de 20: {}'.format(cedulas20))
        if not v:
            break
    if v >= 10:
        cedulas10 = v // 10
        v -= cedulas10 * 10
        print('A quantidade notas de 10: {}'.format(cedulas10))
        if not v:
            break
    if v >= 5:
        cedulas5 = v // 5
        v -= cedulas5 * 5
        print('A quantidade notas de 5: {}'.format(cedulas5))
        if not v:
            break
    if v:
        cedulas1 = v
        print('A quantidade notas de 1: {}'.format(v))
        break
