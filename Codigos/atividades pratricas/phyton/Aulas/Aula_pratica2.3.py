#algoritimo para saber que tipo de Triângulo é

A = int(input( 'Digite um dos lados do Triângulo: '))
B = int(input('Digit)e outro o segundo lado do Triângulo: '))
C = int(input('Digite outro o terceiro lado do Triângulo: '))

if((A> 0 and B > 0 and C > 0) and (A + B >C and A + C > B and B + C >A )):
#Se tudo for atendido é um trinagulo valido 

    if(A != B and A != C and B != C):
        print('Triângulo escaleno')
    else:
        if(A == B and B == C ):
            print('Triângulo equilátero')
        else:
            print('Triângulo isósleces')
else:
    print('Ao menos um dos valores indicado não servem para forma um triangulo. ')
