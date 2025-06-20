'''
integrantes do projeto:
Arthur Colodel
Gabrielly Pereira
Giulia Sitoni
Rafael Silva

senha do gerente: 
admin123

codigo usado para gerar o primeiro cliente e o arquivo pickle:
import pickle
cliente = {
    "nome": "Gaby",
    "saldo": 500.00
}
with open("dados.pkl", "wb") as arquivo:
    pickle.dump(cliente, arquivo)
'''
import pickle

#variaveis globais
menu_cliente = True
menu_gerente = True
menu_principal = True

arquivo = open("dados.pkl","rb")
cliente = pickle.load(arquivo)
arquivo.close

#menu pricipal
while menu_principal == True:
    #interface de navegacao do menu principal
    print("Bem-vindo ao Sistema Bancário!")
    print("Escolha uma opção:")
    print("1: Acessar como cliente")
    print("2: Acessar como gerente")
    print("3: Sair")
    opcao = input("Selecione uma opção: ")
    
    #menu cliente
    if opcao == "1":
        while menu_cliente == True:
            #interface de navegacao do menu cliente
            print("Menu cliente:")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. sacar")
            print("4. Simular rendimento") #OBS: Apresentar mês a mês os próximos doze meses com taxa de 1.1% ao mês.
            print("5. Voltar ao menu principal")
            opcao = input("Escolha uma opção: ")

            #consilta do saldo
            if opcao == "1":
                print(f"ola {cliente["nome"]} seu saldo é: {cliente["saldo"]:.2f} ")
            #realizacao do deposito
            elif opcao == "2":
                print("Selecione a quantia que deseja depositar: ")
                dep = float(input())
                if dep < 0:
                    print("não pode depositar valores negativos")
                else:
                    cliente["saldo"] = cliente["saldo"] + dep
                    #Salva o novo saldo no arquivo
                    arquivo = open("dados.pkl", "wb")
                    pickle.dump(cliente, arquivo)
                    arquivo.close()
                    print(f"deposito realizado com sucesso, saldo atualizado para: {cliente["saldo"]:.2f}")
            #realizacao do saque
            elif opcao == "3":
                print("quantia do qual gostaria de sacar: ")
                saq = float(input())
                if saq < 0:
                    print("Não pode sacar número negativo")
                elif saq > cliente["saldo"]:
                    print("valor não corresponde ao valor de sua conta")
                else:
                    cliente["saldo"] = cliente["saldo"] - saq
                    #Salva o novo saldo no arquivo
                    arquivo = open("dados.pkl", "wb")
                    pickle.dump(cliente, arquivo)
                    arquivo.close()
                    print(f"saque realizado com sucesso, saldo atualizado para: {cliente["saldo"]:.2f}")
            #simulacao de rendimento
            elif opcao == "4": 
                print("1.simular rendimento com saldo: ")
                print("2.simulação com outro valor")
                opicao = int(input())
                #sumula remdimemto com saldo do cliente 
                if opicao == 1:
                    mes = 1
                    rendi = cliente["saldo"]
                    #printa mes a mes o remdimemto de 1.1% sobre o saldo do cliente 
                    while mes != 13:
                        rendi = rendi * 1.011
                        print(f"valor do rendimento do mês {mes} igual a: {rendi:.2f}")
                        mes = mes + 1
                #simula rendimemto com saldo hipotetico
                if opicao == 2:
                    mes = 1
                    rendi = int(input("coloque a quantidade para calculo: "))
                    #printa mes a mes a mes o rendimento de 1.1% sobre saldo hipotetico
                    while mes != 13:
                        rendi = rendi * 1.011
                        print(f"valor do rendimento do mês {mes} igual a: {rendi:.2f}")
                        mes = mes + 1
            #retorna ao memu principal
            elif opcao == "5":
                menu_cliente = False
            #memsagem de erro em caso opcao invalida 
            else:
                print("opcao invalida.")
                
    #autenticacao para menu gerente
    elif opcao == "2":
        tentativas = 0  #Contador de tentativas de senha
        senha_correta = "admin123"
        acesso_liberado = False
        #faz verificacao de senha, com tres tentativas 
        while tentativas < 3 and acesso_liberado == False: #Não acertar a senha e ainda tiver menos de 3 tentativas
            senha = input("Digite a senha do gerente: ")
            if senha == senha_correta:
                acesso_liberado = True
            else:
                tentativas = tentativas + 1
                print(f"Senha incorreta. Tentativa {tentativas} de 3.")
        #acessa menu gerente se acesso liberado
        if acesso_liberado == True: 
            menu_gerente = True
            #menu gerente
            while menu_gerente == True:
                #interface do menu gerente
                print("Menu Gerente:")
                print("1: Cadastrar ou trocar nome do cliente")
                print("2: Corrigir saldo do cliente")
                print("3: Consultar status do cliente")
                print("4: Voltar ao menu principal")
                escolha = input("Escolha uma opção: ")
                
                #da novo nome ao cliente 
                if escolha == "1":
                    novo_nome = input("Digite o novo nome do cliente: ")
                    cliente["nome"] = novo_nome
                    #Salva o novo nome no arquivo com pickle
                    arquivo = open("dados.pkl", "wb")
                    pickle.dump(cliente, arquivo) 
                    arquivo.close()
                    print(f"Nome alterado para: {cliente['nome']}")
                
                #altera saldo do cliente
                elif escolha == "2":
                    novo_saldo = input("Digite o novo saldo: ")
                    cliente["saldo"] = float(novo_saldo)
                    #Salva o novo saldo no arquivo
                    arquivo = open("dados.pkl", "wb")
                    pickle.dump(cliente, arquivo)
                    arquivo.close()
                    print(f"Saldo alterado para: R$ {cliente['saldo']:.2f}")
                
                #consulta nome e saldo do cliente
                elif escolha == "3":
                    print(f"Status do cliente: {cliente['nome']}, Saldo: R$ {cliente['saldo']:.2f}")
                
                #retorna ao menu principal
                elif escolha == "4": 
                    menu_gerente = False
                
                #mensagem de erro em caso de opcao invalida 
                else:
                    print("Opção inválida.")

        # Se excedeu 3 tentativas sem sucesso, volta ao menu principal 
        else:
            print("Acesso bloqueado. Voltando ao menu principal.")
            
    #encerra sistema
    elif opcao == "3":
        print("Saindo...")
        break
    #mensagem de erro em caso de opcao invalida
    else: 
        print("Opção inválida")
