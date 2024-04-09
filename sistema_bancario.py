#SISTEMA BANCARIO
            
saldo = 0 
limite = 500
numero_saques = 0
LIMITE_SAQUE_DIA = 3
extrato = ""

while  True:
    menu = int(input(" [1]Depositar\n [2]Sacar\n [3]Extrato\n [4]Sair " ))
    if menu == 1:
        valor_deposito = float(input("Digite o valor do deposito R$: "))

        status = f"Deposito efetuado com sucesso.\nR$ {valor_deposito}" if valor_deposito > 0 else "Valor não permitido"
        print(f'{status}')
        saldo += valor_deposito
        extrato += f'Deposito: R$ {valor_deposito: 2.2f}\n' 
        
    elif menu ==2:
        valor_saque = float(input("Informe o valor do saque R$: "))
        
        excedeu_saldo = valor_saque > saldo

        excedeu_limite = valor_saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE_DIA

        if excedeu_saldo:
            print("Não foi possivel realizar o saque.\nSaldo insuficiente.")

        elif excedeu_limite:
            print("Não foi possivel realizar o saque.\nValor do saque,acima do limite permitido.")

        elif excedeu_saques:
            print("Não foi possivel realizar o saque.\nNúmero maximo de saques excedido.")

        elif valor_saque > 0:
            saldo -= valor_saque
            extrato += f"Saque: R${valor_saque:12.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso.\nR$ {valor_saque:.2f}")
        else:
            print("Operação negada.\nValor informado inválido")

    elif menu ==3:
        print("\n************EXTRATO*****************\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:12.2f}")
        print("**********************************")

    elif menu == 4:
        break
    else:
        print("Operação invalida")
   


