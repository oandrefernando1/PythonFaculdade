print("Bem-vindo a loja de Gelados do Andre Fernando") # Exibe a mensagem de boas vindas 

# Cardapio da loja
print("--------------------- Cárdapio ---------------------") 
print("------| Tamanho | Cupuaçu (CP) |   Açaí (AC) |------")
print("------|    P    |   R$ 10,00   |   R$ 12,00  |------")
print("------|    M    |   R$ 15,00   |   R$ 17,00  |------")
print("------|    G    |   R$ 19,00   |   R$ 21,00  |------")
print("----------------------------------------------------")

totalpedido = 0  # Inicializa o totalpedido fora do loop

while True: # Estrutura de while para repetir os pedidos
    sabor = input("Digite o sabor desejado (CP/AC):") # Solicitando o sabor desejado pelo usuario
    sabor = sabor.upper()  # Converte o sabor para letras maiúsculas para evitar erros de maiúsculas/minúsculas
    if sabor not in ["CP", "AC"]:
        print("Sabor inválido. Tente novamente.")
        continue # se o usuario digitar algo invalido, volta ao inicio 
    
# Input para o tamanho (P/M/G) com validação
    tamanho = input("\nDigite o tamanho do copo desejado (P/M/G): ")
    tamanho = tamanho.upper() # Converte o tamanho para letras maiúsculas para evitar erros de maiúsculas/minúsculas
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho do copo inválido. Tente novamente.")
        continue # se o usuario digitar algo invalido, volta ao inicio 
    
    #  Calcula o valor do pedido com base no sabor e tamanho
    if sabor == "CP":
        if tamanho == "P":
            valorpedido = 10
        elif tamanho == "M":
            valorpedido = 15
        else:
            valorpedido = 19
    else:  # Se não é "CP", assume-se que é "AC"
        if tamanho == "P":
            valorpedido = 12
        elif tamanho == "M":
            valorpedido = 17
        else:
            valorpedido = 21
    totalpedido += valorpedido  # Acumula o valor do pedido
    print(f"Você escolheu um copo {tamanho} de {sabor} no valor de R${valorpedido:.2f}")
    
    continuar = input("Deseja pedir mais alguma coisa? (S ou N): ")
    if continuar.upper() != "S":
        break
    
print(f"Valor total a ser pago: R${totalpedido:.2f}") # resultado do pedido