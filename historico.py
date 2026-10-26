def ver_historico_txt():
    try:
        linhas = open("equipamentos.txt", "r").readlines()
    except:
        return

    registros = []
    for linha in linhas:
        dados = linha.strip().split(" ")
        registros.append((dados[0], float(dados[1])))

    registros.sort(key=lambda x: x[1], reverse=True)

    posicao = 1
    for item in registros:
        print(posicao, "-", item[0], "-", item[1])
        posicao += 1

    print("Total de linhas/registros:", len(linhas))
