'''
integrantes do grupo:
 > Arthur de Mattos Colodel
 > Rafael Luiz da Silva

 ITEM 2
Sistema de cadastro e login com:
 > nome e senha de 4 digitos
 > altenticação via hash
'''
import hashlib

print ('')
i = 0

# loop do programa principal 
while(i == 0):
    print('1. criar conta')
    print('2. logar na conta.')
    print('*. sair.')
    escolha = input('... ')
    
    # Criação do Usuário
    if(escolha == '1'):
        print('Criação de conta')
        nome = input('digite seu nome de 4 digitos: ')
        senha = input('digite sua senha de 4 digitos: ')
        
        #verificação de tamanho para nome e senha
        if(len(nome) > 4 or len(nome) < 4):
            print('''O tamanho da nome foge do padrão de 4 digitos
        Por favor, tente novamente
            ''')
        elif(len(senha) > 4 or len(senha) < 4):
            print('''O tamanho da senha foge do padrão de 4 digitos
        Por favor, tente novamente
            ''')
        else:
            # cria hash da senha 
            codigoMd5 = hashlib.md5(senha.encode())
            codigoMd5 = codigoMd5.hexdigest()

            # Salva dados em dados.txt
            with open('dados.txt', 'a') as arquivo:
                arquivo.write(f'{nome},{codigoMd5}\n')
                print("dados salvos")
    
    # Logar no usuario
    elif(escolha == '2'):
        print("Login: ")
        nomeUsuario = input('Nome de Usuario: ')
        hashSenhaUsuario = input('Senha de Usuario: ')
        nome = ""
        hashSenha = ""
        
        # cria hash da senha 
        codigoMd5 = hashlib.md5(hashSenhaUsuario.encode())
        hashSenhaUsuario = codigoMd5.hexdigest()
        # busca dados em dados.txt
        with open('dados.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            
            # Procura usuário
            for linha in linhas:
                conta = linha.split(",")
                nome = conta[0]
                hashSenha = conta[1].replace("\n","")
                if (nomeUsuario == nome and hashSenhaUsuario == hashSenha):
                    break
            # Faz processo de autenticacao
            if (nomeUsuario == nome and hashSenhaUsuario == hashSenha):
                i += 1
                print('Logado com sucesso')
            else:
                print('nome ou senha do usuario incorretos')
    else:
        i += 1
                
