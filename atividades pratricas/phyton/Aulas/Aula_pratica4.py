def valida_int(pergunta, min , max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fatorial (num):

    """
    função que calcular a fatorial de um numero interio  
    :para num:
    :return:
    """

    fat = 1
    if num == 0:
        return fat 
#Essa parte só vai executar caso num > 0 
    for i in range(1, num + 1):
        fat *= i
    return fat

x = int(input('Digite um valor para calcular o fatorial: '))
x = valida_int('Digite um valor para calcular o fatorial: ', 0, 99999999999)
print(f'{x}! = {fatorial(x)}')

