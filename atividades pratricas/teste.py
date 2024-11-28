"""def valida_sabor(sabor):
    return sabor in ['PS', 'PD']

def valida_tamanho(sabor, tamanho):
    tamanhos_validos = {'PS': {'P': 30, 'M': 45, 'G': 60}, 'PD': {'P': 34, 'M': 48, 'G': 66}}
    return tamanho in tamanhos_validos[sabor]

def obter_sabor():
    while True:
        sabor = input('Digite o sabor (PS/PD): ').upper()
        if valida_sabor(sabor):
            return sabor
        print('Sabor inválido. Digite PS ou PD.')

def obter_tamanho(sabor):
    while True:
        tamanho = input('Digite o tamanho (P/M/G): ').upper()
        if valida_tamanho(sabor, tamanho):
            return tamanho
        print('Tamanho inválido para o sabor escolhido.')

def calcular_preco(sabor, tamanho):
    tamanhos_validos = {'PS': {'P': 30, 'M': 45, 'G': 60}, 'PD': {'P': 34, 'M': 48, 'G': 66}}
    return tamanhos_validos[sabor][tamanho]

# Dicionário para mapear os valores curtos para os nomes completos
sabores = {'PS': 'pizza salgada', 'PD': 'pizza doce'}

valor_total = 0

while True:
    sabor = obter_sabor()
    tamanho = obter_tamanho(sabor)
    preco = calcular_preco(sabor, tamanho)

    valor_total += preco

    continuar = input('Deseja continuar? (S/N): ').upper()
    if continuar == 'N':
        break

# Ao final, mostramos apenas o valor total
print(f"O valor total da sua compra é R$ {valor_total:.2f}")"""
# Print do nome completo
print("Bem-vindos a Madeireira do André Rezende Finco")
print(" ")
print("Entre com o Tipo de Madeira desejado:")
print("PIN - Tora de Pinho")
print("PER - Tora de Peroba")
print("MOG - Tora de Mogno")
print("IPE - Tora de Ipê")
print("IMB - Tora de Imbuia")

# Dicionário com preços por m³ de cada tipo de madeira
preco_madeira = {
    "PIN": 150.40,  # Preço por m³ da Tora de Pinho
    "PER": 170.20,  # Preço por m³ da Tora de Peroba
    "MOG": 190.90,  # Preço por m³ da Tora de Mogno
    "IPE": 210.10,  # Preço por m³ da Tora de Ipê
    "IMB": 220.70   # Preço por m³ da Tora de Imbuia
}

# Função para escolher o tipo de madeira
def escolha_tipo():
    while True:
        tipoMadeira = input(">>").upper()
        if tipoMadeira in preco_madeira:
            return preco_madeira[tipoMadeira]
        print("Opção inválida. Por favor, escolha entre PIN, PER, MOG, IPE, IMB.")

# Função para escolher a quantidade de toras e calcular desconto
def qtd_toras():
    while True:
        try:
            qtdToras = int(input("Entre com a quantidade de toras (em m³): "))
            if qtdToras > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. Por favor, entre com a quantidade novamente. (O limite é 2000 m³).")
                continue
            elif qtdToras < 100:
                return qtdToras, 0  # Sem desconto
            elif 100 <= qtdToras < 500:
                return qtdToras, 0.04  # Desconto de 4%
            elif 500 <= qtdToras < 1000:
                return qtdToras, 0.09  # Desconto de 9%
            elif 1000 <= qtdToras <= 2000:
                return qtdToras, 0.16  # Desconto de 16%
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Função para escolher o tipo de transporte
def transporte():
    while True:
        print("")
        print("Escolha o tipo de Transporte:")
        print("1 - Transporte Rodoviário - R$ 1000.00")
        print("2 - Transporte Ferroviário - R$ 2000.00")
        print("3 - Transporte Hidroviário - R$ 2500.00")
        trans = input(">>")
        if trans == "1":
            return 1000.00  # Transporte Rodoviário
        elif trans == "2":
            return 2000.00  # Transporte Ferroviário
        elif trans == "3":
            return 2500.00  # Transporte Hidroviário
        print("Opção inválida. Escolha entre 1, 2 ou 3.")

# Código principal
try:
    valor_madeira = escolha_tipo()  # Obtém o valor da madeira
    qtdToras, desconto = qtd_toras()  # Obtém a quantidade e o desconto
    valor_transporte = transporte()    # Obtém o valor do transporte

    # Cálculo do total
    total = (valor_madeira * qtdToras) * (1 - desconto) + valor_transporte

    # Exibe o total do pedido
    print(f"Total a pagar: R$ {total:.2f}")

except Exception as e:
    print(f"Ocorreu um erro: {e}")