import csv
import json

def cadastrar_equipamento():
    nome = input("Nome do Equipamento: ")
    patrimonio = input("Patrimônio/Ano: ")
    valor = float(input("Valor/Custo: "))

    arquivo_txt = open("equipamentos.txt", "a")
    arquivo_txt.write(nome + " " + str(valor) + "\n")
    arquivo_txt.close()

    with open("equipamentos.csv", "a", newline="") as arquivo_csv:
        csv.writer(arquivo_csv).writerow([nome, patrimonio, valor])

    try:
        with open("equipamentos.json", "r", encoding="utf-8") as arquivo_json:
            lista = json.load(arquivo_json)
    except:
        lista = []

    lista.append({"nome": nome, "idade": patrimonio, "pontuacao": valor})

    with open("equipamentos.json", "w", encoding="utf-8") as arquivo_json:
        json.dump(lista, arquivo_json, indent=4, ensure_ascii=False)


  



    