# --- Variáveis Iniciais ---
saldo = 0
limite_por_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

# --- Menu Principal ---
menu = """
=============== MENU ===============
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
====================================
=> """

while True:

    opcao = input(menu).lower()

    # --- Operação de Depósito ---
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:  R$ {valor:.2f}\n" 
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido (deve ser positivo).")

    # --- Operação de Saque ---
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        # Verifica as condições de falha
        excedeu_saldo = valor > saldo
        excedeu_limite_saque = valor > limite_por_saque
        excedeu_num_saques = numero_saques >= LIMITE_SAQUES_DIARIOS

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido (deve ser positivo).")

        elif excedeu_saldo:
            print(f"Operação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo:.2f})")

        elif excedeu_limite_saque:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por operação.")

        elif excedeu_num_saques:
            print(f"Operação falhou! Número máximo de {LIMITE_SAQUES_DIARIOS} saques diários atingido.")

        # Se passou em todas as verificações
        else:
            saldo -= valor
            extrato += f"Saque:     R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    # --- Operação de Extrato ---
    elif opcao == "e":
        print("\n=============== EXTRATO ===============")
        
        if not extrato: 
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=====================================")

    # --- Sair ---
    elif opcao == "q":
        print("Saindo do sistema... Obrigado!")
        break 

    # --- Opção Inválida ---
    else:
        print("Operação inválida! Por favor, selecione novamente a operação desejada.")