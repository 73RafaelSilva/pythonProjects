import random

charset = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9',';',':','!','?','@','#','$','%','*','&','(',')',',','.','[',']','=','+','-','_','{','}',' ']

for i in range(0,4):
    senha = ""
    for j in range(0,4):
        digito = random.randint(0,len(charset))
        senha += charset[digito]
    print(senha)
