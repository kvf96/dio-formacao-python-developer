from datetime import datetime
data_hora = datetime.now()
menu = """
************* BANCO DIO ***************
Informe a operação que deseja:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

***************************************
=> """

saldo = 1000
limite = 2000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 10

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}    Data: {data_hora}\n"
        else:
            print("Operação falhou! O valor informadao é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo-= valor
            extrato += f"   Saque: R${valor:.2f}    Data: {data_hora}\n"
            numero_saques += 1
       
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n*************** EXTRATO ***************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo na conta: R$ {saldo:.2f}")
        print("\n***************************************")
    elif opcao == "q":
        break
    else:
        print("Operação Inválida! Por favor, selecione a operação desejada.")