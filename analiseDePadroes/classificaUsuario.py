'''
integrantes:
    > Arthur Colodel
    > Gabrielly Pereira
    > Giulia Sitoni
    > Rafael Silva

Código para a classificação de usuários, comparando-os aos usuários já classificados.

Cenário:
desenvolver um sistema que analisa o comportamento de usuários conectados à rede de um laboratório de informática.

A equipe de infraestrutura coletou os seguintes dados de uso da rede:
    - Download médio diário (MB)
    - Upload médio diário (MB)
    - Número médio de acessos simultâneos
    - Tempo médio de conexão por dia (em minutos)

Com base nesses dados, os usuários foram classificados em três perfis:
    - P1 – Uso leve: navegação básica, poucos downloads, acessos pontuais
    - P2 – Uso moderado: streaming, videoconferências, tempo de uso médio
    - P3 – Uso intenso: desenvolvedores, gamers ou usuários que manipulam arquivos grandes
'''

import math

# lista de usuarios da base de dados ja classificados
database = [[120, 10, 3, 250, 'P1'],
        [200, 25, 5, 400, 'P2'],
        [80, 5, 2, 180, 'P1'],
        [300, 30, 6, 500, 'P3'],
        [250, 40, 7, 600, 'P3'],
        [150, 12, 4, 320, 'P2'],
        [90, 8, 3, 200, 'P1'],
        [310, 35, 6, 520, 'P3'],
        [170, 15, 4, 350, 'P2'],
        [85, 6, 2, 190, 'P1'],
        [220, 18, 5, 410, 'P2'],
        [305, 38, 6, 510, 'P3'],
        [130, 11, 3, 270, 'P1'],
        [260, 42, 7, 580, 'P3'],
        [160, 14, 4, 330, 'P2'],
        [100, 9, 2, 210, 'P1'],
        [240, 28, 6, 460, 'P3'],
        [180, 16, 4, 370, 'P2'],
        [95, 7, 2, 195, 'P1'],
        [270, 40, 6, 590, 'P3']]

# lista de novos usuarios
novosUsuarios = [[110, 9, 3, 220],
                [190, 17, 4, 380],
                [275, 36, 6, 540],
                [140, 13, 3, 300],
                [230, 20, 5, 430]]



# roda o bloco de codigo uma vez para cada novo usuario da lista
for pessoa in novosUsuarios:
    # guarda a classificação do novo usuario
    addiciona = ""
    i = 9999

    # calcula distancia entre cada novo usuario e todos os usuarios do banco de dados
    for usuario in database:
        sum = 0
        for j in range(0,4):
            sum = sum + ((pessoa[j] - usuario[j]) ** 2)
        sum = int(math.sqrt(sum))

        # encontra a qual classificação do usuario
        if i > sum:
            i = sum
            addiciona = usuario[4]

    # adciona classificação do usuario ao fim de sua lista
    pessoa.append(addiciona)
    print(pessoa)
        