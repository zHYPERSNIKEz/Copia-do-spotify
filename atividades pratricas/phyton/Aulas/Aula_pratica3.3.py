valor = int(input("Digite o valor em R$: "))
 
while True:
    if ( valor >= 100):
      cont100 = valor // 100
      print(f'Cédulas de 100: {cont100}')
      if not valor:
        break
      
    if ( valor >= 50):
      cont50 = valor // 50
      print(f'Cédulas de 50: {cont50}')
      if not valor:
        break
      
    if ( valor >= 20):
      cont20 = valor // 20
      print(f'Cédulas de 20: {cont20}')
      if not valor:
        break
    if ( valor >= 10):
      cont10 = valor // 10
      print(f'Cédulas de 10: {cont10}')
      if not valor:
        break


    if ( valor >= 5):
      cont5 = valor // 5
      print(f'Cédulas de 5: {cont5}')
      if not valor:
        break
      
    if valor:
        cont1 = valor
        print(f'Cédulas de 1: {cont1}')
        break
         
      
valor = int(input("Digite o valor em R$: "))

while valor > 0:
    if valor >= 100:
        cont100 = valor // 100
        valor %= 100
        print(f'Cédulas de 100: {cont100}')
    elif valor >= 50:
        cont50 = valor // 50
        valor %= 50
        print(f'Cédulas de 50: {cont50}')
    elif valor >= 20:
        cont20 = valor // 20
        valor %= 20
        print(f'Cédulas de 20: {cont20}')
    elif valor >= 10:
        cont10 = valor // 10
        valor %= 10
        print(f'Cédulas de 10: {cont10}')
    elif valor >= 5:
        cont5 = valor // 5
        valor %= 5
        print(f'Cédulas de 5: {cont5}')
    elif valor >= 2:
        cont2 = valor // 2
        valor %= 2
        print(f'Cédulas de 2: {cont2}')
    else:
        cont1 = valor
        valor = 0
        print(f'Cédulas de 1: {cont1}')
