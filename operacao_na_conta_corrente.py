# Criar um sistema bancário simples com as opções sacar, depositar e visualizar saldo.
# Versão 1.0
# Implementar 3 funções: sacar, depositar e visualizar saldo.
# Essa versão Possui apenas um usuário


print("Bem-vindo ao sistema bancário!")

# Menu de opções
menu = """
===== Escolha uma opção =====

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_DIARIO_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        # Opção de depósito
        print("Depósito")
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        # todos os depósitos devem ser armazenados em uma variável e ser exibido na operação de extratos
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
        else:
            print("Valor inválido para depósito.")

    # Opção de saque
    # A opção de saque dever permitir 3 saques diários
    elif opcao == "s":
        # Verificar se o número de saques diários não excede o limite
        if numero_saques >= LIMITE_DIARIO_SAQUES:
            print("Número máximo de saques diários atingido.")
            continue
        # Solicitar o valor do saque
        print("Sacar")
        valor_saque = float(input("Digite o valor do saque: R$ "))
        # Verificar se o valor do saque é maior que zero.
        if valor_saque <= 0:
            print("Valor de saque inválido. Deve ser maior que zero.")
            continue
        # Verificar se o limite máximo é de R$ 500,00 por saque
        if valor_saque > limite:
            print(f"Valor excede o limite por saque de R$ {limite:.2f}.")
            continue
        # Verificar se o valor do saque é maior que o saldo.
        if valor_saque > saldo:
            print("Saldo insuficiente para realizar o saque.")
            continue
        # todos os saques devem ser armazenados em uma variável e ser exibido na operação de extratos.
        if valor_saque > 0 and numero_saques < LIMITE_DIARIO_SAQUES and valor_saque <= saldo:
            saldo -= valor_saque
            extrato += f"Saque:    R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
        else:
            print("Saque não permitido. Saldo insuficiente")
        
    # Opção de extrato
    elif opcao == "e":
        print("\n=== Extrato ===")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================")
    
    # Opção de sair
    elif opcao == "q":
        print("Sair")
        # Exibir mensagem de encerramento
        print("\nObrigado por utilizar nosso sistema bancário!")
        print("Até logo!")
        break
    
    # Opção inválida
    else:
        print("Opção inválida. Por favor, solicite novamente a opção desejada.")
# Fim do loop

