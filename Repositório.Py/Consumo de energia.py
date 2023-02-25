kwh = float(input('\nDigite a quantidade kWh consumida: '))
ti = input('\nPara qual tipo de instalação? (R: Residencial, C: Comércio) ou I: Indústrial:')

R = ti
C = ti
I = ti
div = kwh / 0.40
div2 = kwh // 0.65
div3 = kwh // 0.55
div4 = kwh / 0.60

if ti == R and kwh <= 500:
    print('\nO valor residencial até ''500kWh'' é de: ${}'.format(div))
elif kwh > 500:
    print('\nO valor residencial acima de ''500kWh'' é de: ${}'.format(div2))
elif ti == C and kwh <= 100:
    print('\nO valor comercial até ''100kWh'' é de: ${}'.format(div3))
elif kwh > 1000:
    print('\nO valor comercial acima de ''1000kWh'' é de: ${}'.format(div4))
elif ti == I and kwh <= 5000:
    print('\nO valor indústrial até ''5000kWh'' é de: ${}'.format(div3))
elif kwh > 5000:
    print('\nO valor indústrial acima de ''5000kWh'' é de: ${}'.format(div4))