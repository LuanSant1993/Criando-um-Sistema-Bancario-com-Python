import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito Realizado Com Sucesso! ===")
    else:
        print("\n@@@ Operação Falhou! O Valor Informado é Inválido. @@@")
        
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("\n@@@ Operação Falhou! Você Não Tem Saldo Suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação Falhou! O Valor do Saque Excede o Limite. @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação Falhou! Número Máximo de Saques Excedido. @@@")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque Realizado com Sucesso! ===")
        
    else:
        print("\n@@@ Operação Falhou! O Valor Informado é Inválido. @@@")
        
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já Existe Usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu Nome Completo: ")
    data_nascimento = input("Informe a sua Data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o seu Endereço (Rua, Número - Bairro - Cidade/Sigla Estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "CPF": cpf, "endereco": endereco})
    
    print("=== Usuário Criado com Sucesso ===")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta Criada com Sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário Não Encontrado, Fluxo de Conta Encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\ 
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}   
            Titular:\t{conta["usuario"]["nome"]}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))
         
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor  = float(input("Informe o Valor do Depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float(input("Informe o Valor do Saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            
        elif opcao ==  "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Operação Inválida, Por Favor Selecione Novamente a Operação Desejada")
            
main()
