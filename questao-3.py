# Exibe a mensagem de boas-vindas
print("Bem-vindo a Lan House do Andre Fernando!")

# Função para escolher o serviço
def escolha_servico():
    while True:
        # Solicita ao usuário que escolha um tipo de serviço desejado
        print("\nEscolha um tipo de serviço desejado:")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IBO - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        escolha = input("Digite o serviço desejado: ")
        escolha = escolha.lower()  # Converte a entrada para minúsculas para ser insensível a maiúsculas/minúsculas
        if escolha in ["dig", "ico", "ibo", "fot"]:  # Verifica se a escolha está entre as opções válidas
            return escolha  # Retorna o serviço escolhido
        else:
            print("\nOpção inválida.\nEntre com o tipo de serivo desejado")  # Exibe uma mensagem de erro se a escolha for inválida

# Função para calcular o número de páginas com desconto
def num_pagina():
    while True:
        num_paginas = int(input("\nDigite o número de páginas: "))  # Solicita ao usuário que insira o número de páginas
        if num_paginas < 10:
            return num_paginas  # Se o número de páginas for inferior a 10, não há desconto
        elif 10 <= num_paginas < 100:
            return int(num_paginas * 0.9)  # Se o número de páginas estiver entre 10 e 99, aplica um desconto de 10%
        elif 100 <= num_paginas < 1000:
            return int(num_paginas * 0.85)  # Se o número de páginas estiver entre 100 e 999, aplica um desconto de 15%
        elif 1000 <= num_paginas < 10000:
            return int(num_paginas * 0.8)  # Se o número de páginas estiver entre 1000 e 9999, aplica um desconto de 20%
        else:
            print("\nNão aceitamos tantas paginas de uma só vez!\nPor favor entre com um numero menor de paginas!")  # Exibe uma mensagem de erro se o número de páginas não se encaixar nas faixas acima

# Função para escolher serviços adicionais
def servico_extra():
    extra = 0
    while True:
        # Solicita ao usuário que escolha um serviço adicional
        print("\nEscolha um serviço adicional:")
        print("1 - Encadernação simples - R$ 10.00")
        print("2 -Encadernação de capa dura - R$ 25.00")
        print("0 - Não desejo mais nada")
        adicional = input("Digite o serviço adicional desejado: ")
        if adicional == "1":
            extra += 10
        elif adicional == "2":
            extra += 25
        elif adicional == "0":
            return extra
        else:
            print("Opção inválida.")  # Exibe uma mensagem de erro se a escolha for inválida     
try:
    # Chamando a função para escolher o serviço
    servico = escolha_servico()
    
    # Chamando a função para calcular o número de páginas com desconto
    num_paginas_desconto = num_pagina()
    
    # Chamando a função para escolher serviços adicionais
    extra = servico_extra()
    
    # Calculando o total a pagar com base no serviço escolhido
    if servico == "dig":
        valor_servico = num_paginas_desconto * 1.10
    elif servico == "ico":
        valor_servico = num_paginas_desconto * 1.00
    elif servico == "ibo":
        valor_servico = num_paginas_desconto * 0.40
    elif servico == "fot":
        valor_servico = num_paginas_desconto * 0.20
    else:
        print("Opção de serviço inválida.")
    
    total = valor_servico + extra  # Calculando o total a pagar
    
    # Exibindo o resumo do pedido
    print("\nResumo do Pedido:")
    print(f"Serviço: {servico}")
    print(f"Número de Páginas com Desconto: {num_paginas_desconto}")
    print(f"Valor do Serviço: R$ {valor_servico:.2f}")
    print(f"Valor dos Serviços Adicionais: R$ {extra:.2f}")
    print(f"Total a Pagar: R$ {total:.2f}")
    
except ValueError:
    print("Entrada inválida. Certifique-se de digitar números corretamente.")
