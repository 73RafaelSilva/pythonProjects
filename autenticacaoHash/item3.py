'''
integrantes do grupo:
 > Arthur de Mattos Colodel
 > Rafael Luiz da Silva

 ITEM 3
Código de força bruta para quebrar o hash MD5.
 > tenta senhas de 4 caracteres
 > charset de 84 caracteres
 > quebra senha de 4 contas
'''

import hashlib
import time

charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',';',':','!','?','@','#','$','%','*','&','(',')',',','.','[',']','=','+','-','_','{','}',' ']
tentativa = ""
senhasEncontradas = 0
inicio = time.time()
linhas = []

# Lê e salva dados das contas
with open('dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
with open("senhasQuebradas.txt", 'w') as arquivo:
    arquivo.write(f"############################################\n")
contas = len(linhas)
if (contas > 3):
    contas = 4


print("executando. . . ")

#percorrendo todas as possibilidades de senha
for i in charset:
    for j in charset:
        for k in charset:
            for l in charset:
                tentativa = i + j + k + l

                # cria hash da tentativa 
                codigoMd5 = hashlib.md5(tentativa.encode())
                hashTentativa = codigoMd5.hexdigest()

                
                tam = len(linhas)
                idx = 0
                # permite que a tentativa seja comparada com cada hash de cada conta
                while(idx < tam):
                    conta = linhas[idx].split(",")
                    nome = conta[0]
                    hashSenha = conta[1].replace("\n","")

                    # compara hash da tentativa com o hash da conta para descobrir sua senha
                    if(hashTentativa == hashSenha):
                        #salva Contas com senhas descobertas
                        fim = time.time()                    
                        tempoExecucao = fim - inicio
                        with open("senhasQuebradas.txt", 'a') as arquivo:
                            arquivo.write(f"\nNome: {nome} \nSenha: {tentativa} \nhash da senha: {hashTentativa} \ntempo de quebra de senha: {tempoExecucao:.2f} segundos\n")

                        linhas.remove(linhas[idx])
                        tam -=1
                        idx -=1
                        
                        senhasEncontradas += 1

                        #condicao de parada em cascata
                        if (senhasEncontradas == contas):
                            break
                    idx +=1
                if(senhasEncontradas == contas):
                    break
            if(senhasEncontradas == contas):
                break
        if(senhasEncontradas == contas):
            break
    if(senhasEncontradas == contas):
        break

with open("senhasQuebradas.txt", 'a') as arquivo:
    arquivo.write(f"\n############################################\n")
print('Fim da execução.')
