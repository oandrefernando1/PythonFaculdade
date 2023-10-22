print("\nSeja bem-vindo a loja do Andre Fernando!") #Exibe a mensagem de boas vindas 
 
valortotal = float(input('Digite o valor unitario do produto: ')) # Solicita o valor unitario do produto 
quantidade = int(input('Digite a quantidade do produto: ')) # Solicita a quantidade do produto 
  
valorsemdesconto = valortotal * quantidade # Calcula o valor do produto total sem desconto
 
if valorsemdesconto <= 0: # Verifica se foi digitado o valor valido
    print('Valor inválido!') 
 
elif valorsemdesconto <= 1000: 
    print('O valor total é de: {} Reais'.format(valorsemdesconto)) # Exibe na tela o Valor total SEM desconto 
 
elif valorsemdesconto >= 1000 and valorsemdesconto < 3000:
    resultdesconto = valorsemdesconto * (1 - 0.03) # Multiplica o valor sem desconto com a margem do valor para aplicar a % correta de desconto
    print('O valor total SEM desconto é de: {:.2f} Reais'.format(valorsemdesconto)) # Exibe na tela o valor SEM desconto
    print('O valor total COM desconto de 3% é de: {:.2f} Reais'.format(resultdesconto)) # Exibe na tela o valor COM desconto
 
elif valorsemdesconto >= 3000 and valorsemdesconto < 5000:
    resultdesconto = valorsemdesconto * (1 - 0.05) # Multiplica o valor sem desconto com a margem do valor para aplicar a % correta de desconto
    print('O valor total SEM desconto é de: {:.2f} Reais'.format(valorsemdesconto)) # Exibe na tela o valor SEM desconto
    print('O valor total COM desconto de 3% é de: {:.2f} Reais'.format(resultdesconto)) # Exibe na tela o valor COM desconto
 
elif valorsemdesconto >= 5000:
    resultdesconto = valorsemdesconto * (1 - 0.08) # Multiplica o valor sem desconto com a margem do valor para aplicar a % correta de desconto 
    print('O valor total SEM desconto é de: {:.2f} Reais'.format(valorsemdesconto)) # Exibe na tela o valor SEM desconto
    print('O valor total COM desconto de 3% é de: {:.2f} Reais'.format(resultdesconto)) # Exibe na tela o valor COM desconto
else: 
    print('Ocorreu um erro, tente novamente!') # Exibe uma mensagem caso nenhuma opcao a cima seja executada
 