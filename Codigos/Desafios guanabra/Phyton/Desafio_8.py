#programa para ler um numero e traser de volta o numero em cenimentro e em milimentros 

valor = float(input ('Digite aqui seu numero em mentros: '))

cm = valor * 100
mm = valor * 1000

print(f'O {valor} em centimentros é {cm:.0f} e em milimentros é {mm:.0f}')