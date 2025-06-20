
'''
atividade Cifra de Cesar
'''
key = 1
j = 0
i = 0

amostra = "abcdefghijklmnopqrstuvwxyz .,!?"
frase = "if keep a secret, you must also hide it from yourself."
fraseCifrada = ""

print (frase)
tamanhoAmostra = len(amostra)
tamanhoFrase = len(frase)

while tamanhoFrase!= i:
    j = 0
    while tamanhoAmostra != j:
        if(amostra[j] == frase[i]):
            posicaoNovaLetra = j + key
            print("nova letra")
            while posicaoNovaLetra >= tamanhoAmostra:
                posicaoNovaLetra -= tamanhoFrase
            fraseCifrada += amostra[posicaoNovaLetra]
        j += 1
    i += 1
    
print(fraseCifrada)
print(len(fraseCifrada))
print(len(frase))