print("Olá, bem-vindo ao Banco X")

# ---------- FUNÇÕES ----------
def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_nome(nome):
    return nome.replace(" ", "").isalpha()

def validar_senha(senha):
    return senha.isdigit() and len(senha) == 6

clientes = []

def criar_cliente():
    nome = input("Nome completo: ").strip()
    cpf = input("CPF (11 dígitos): ").strip()
    senha = input("Crie sua senha numérica(6 dígitos): ").strip()
    if not validar_nome(nome) or not validar_cpf(cpf) or not validar_senha(senha):
        print("Dados inválidos.")
        return

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("CPF já cadastrado.")
            return

    clientes.append({
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "saldo": 2000.0
    })

    print(f"Conta cadastrada com sucesso! Bem-vindo(a), {nome}!")

def atualizar_senha(cliente):
    nova_senha = input("Digite sua nova senha (6 dígitos): ").strip()

    if not validar_senha(nova_senha):
        print("Senha inválida.")
        return

    cliente["senha"] = nova_senha
    print("Senha atualizada com sucesso!")

def buscar_cliente(cpf, senha):
    for cliente in clientes:
        if cliente["cpf"] == cpf and cliente["senha"] == senha:
            return cliente
    return None

# ---------- SISTEMA ----------
while True:
    print("\nDeseja criar uma conta ou fazer login?")
    print("1 - Criar conta")
    print("2 - Login")
    print("0 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        criar_cliente()

    elif escolha == "2":
        print("\n=== LOGIN ===")
        cpf = input("CPF: ")
        senha = input("Senha: ")

        cliente = buscar_cliente(cpf, senha)

        if not cliente:
            print("CPF ou senha incorretos.")
            continue

        print(f"Login realizado com sucesso! Bem-vindo(a), {cliente['nome']}")

        while True:
            print("\n== Menu Principal ==")
            print("1 - Ver saldo")
            print("2 - Saque")
            print("3 - Depósito")
            print("4 - Pix")
            print("5 - Alterar senha")
            print("6 - Logoff")

            opcao = input("Selecione a opção desejada: ")

            if opcao == "1":
                print(f"Seu saldo é: R$ {cliente['saldo']:.2f}")

            elif opcao == "2":
                saque = float(input("Valor do saque: R$ "))
                if saque > cliente["saldo"]:
                    print("Saldo insuficiente.")
                else:
                    cliente["saldo"] -= saque
                    print(f"Saldo atual: R$ {cliente['saldo']:.2f}")

            elif opcao == "3":
                deposito = float(input("Valor do depósito: R$ "))
                cliente["saldo"] += deposito
                print(f"Saldo atual: R$ {cliente['saldo']:.2f}")

            elif opcao == "4":
                pix = float(input("Valor do pix: R$ "))
                if pix > cliente["saldo"]:
                    print("Saldo insuficiente.")
                else:
                    cliente["saldo"] -= pix
                    print(f"Saldo atual: R$ {cliente['saldo']:.2f}")

            elif opcao == "5":
                atualizar_senha(cliente)

            elif opcao == "6":
                print("Realizando logoff...")
                break

            else:
                print("Opção inválida.")

    elif escolha == "0":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida.")