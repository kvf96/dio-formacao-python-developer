from datetime import datetime
import textwrap
data_hora = datetime.now()

def menu():
    menu = """
    
    ************* BANCO DIO ***************

    Informe a operação que deseja:

     [d] Depositar
     [s] Sacar
     [e] Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] listar Contas
     [q] Sair

    ***************************************
    
    => """
    return input(textwrap.dedent(menu))

# A função depósito deve receber os argumentos apenas por posição (tudo antes de '/' deve ser passado por posição)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}    Data: {data_hora}\n"
        print("\nOperação concluída com sucesso!")
    else:
        print("\nOperação falhou! O valor informadao é inválido.")
    return saldo, extrato

# A função saque deve receber os argumentos apenas por nome
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor de saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"   Saque: R${valor:.2f}    Data: {data_hora}\n"
        numero_saques += 1
        print("\nOperação concluída com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato

# A função extrato deve receber os argumentos por posição e nome
def consulta_extrato(saldo, /, *, extrato):
    print("\n*************** EXTRATO ***************")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo na conta: R$ {saldo:.2f}")
    print("\n***************************************")

# A função deve cadastrar os usuarios em lista
def cadastrar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números):")
    usuario = listar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, numero - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!")

# A função deve cadastrar a conta em lista
def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF: ")
    usuario = listar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado!")

def listar_usuario(cpf, usuarios):
    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência: \t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 10
    AGENCIA = "0001"

    saldo = 1000
    limite = 2000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("\nInforme o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("\nInforme o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            consulta_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            cadastrar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\nOperação Inválida! Por favor, selecione a operação desejada.")

main()

