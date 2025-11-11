def depositar(saldo, extrato, /):
    """
    Realiza a operação de depósito.
    Recebe saldo e extrato, solicita valor ao usuário,
    valida se é positivo e retorna o novo saldo e extrato.
    """
    valor = float(input("Informe o valor do depósito: R$ "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:  R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido (deve ser positivo).")
        
    return saldo, extrato


def sacar(*, saldo, extrato, numero_saques, limite_por_saque, limite_saques_diarios):
    """
    Realiza a operação de saque.
    Recebe todos os dados da conta, solicita valor ao usuário,
    valida todas as regras de negócio (saldo, limites) e 
    retorna o novo saldo, extrato e número de saques.
    """
    valor = float(input("Informe o valor do saque: R$ "))

    # Verifica as condições de falha
    excedeu_saldo = valor > saldo
    excedeu_limite_saque = valor > limite_por_saque
    excedeu_num_saques = numero_saques >= limite_saques_diarios

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido (deve ser positivo).")

    elif excedeu_saldo:
        print(f"Operação falhou! Saldo insuficiente. (Saldo atual: R$ {saldo:.2f})")

    elif excedeu_limite_saque:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por operação.")

    elif excedeu_num_saques:
        print(f"Operação falhou! Número máximo de {limite_saques_diarios} saques diários atingido.")

    # Se passou em todas as verificações
    else:
        saldo -= valor
        extrato += f"Saque:     R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Recebe saldo e extrato, e imprime na tela
    as movimentações e o saldo final.
    """
    print("\n=============== EXTRATO ===============")
    
    if not extrato: 
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=====================================")


def main():
    """
    Função principal que executa o sistema bancário.
    """
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
            # Atualiza as variáveis com os valores retornados pela função
            saldo, extrato = depositar(saldo, extrato) 

        # --- Operação de Saque ---
        elif opcao == "s":
            # Atualiza as variáveis com os valores retornados pela função
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                limite_por_saque=limite_por_saque,
                limite_saques_diarios=LIMITE_SAQUES_DIARIOS
            )

        # --- Operação de Extrato ---
        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        # --- Sair ---
        elif opcao == "q":
            print("Saindo do sistema... Obrigado!")
            break 

        # --- Opção Inválida ---
        else:
            print("Operação inválida! Por favor, selecione novamente a operação desejada.")

# --- Executa o programa ---
main()