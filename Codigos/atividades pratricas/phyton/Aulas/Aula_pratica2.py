#Teste de idade  
idade = int(input("Digite sua idade: "))
if idade >= 60:
    print(f"Sua idade é {idade}, então você tem direito ao benefício ^~^")
else:
    print(f'Sua idade ainda não atingiu o mínimo para receber o benefício')

#Teste de dano 
dano = int(input("Digiter o dano recebedio: "))
escudo = 10

if dano >= 10:
    print("Você está morto")
else:
    print("Você sobreviveu")

#Teste logico 
norte = True
sul = False
leste = False
oeste = False

if(norte == True or sul == True or leste == True or oeste == True):
    print("Você escapou")

