import csv

def listar_inventario_csv():
    try:
        with open("equipamentos.csv", "r") as arquivo_csv:
            leitor = list(csv.reader(arquivo_csv))
    except:
        return

    soma_valores = 0
    maior_valor = -1.0
    item_mais_valioso = ""

    for linha in leitor:
        if linha:
            nome, patrimonio, valor = linha[0], linha[1], float(linha[2])
            print(nome, "-", patrimonio, "-", valor)
            
            soma_valores += valor
            if valor > maior_valor:
                maior_valor = valor
                item_mais_valioso = nome

    total = len(leitor)
    if total > 0:
        print("Total de equipamentos:", total)
        print(f"Média de valor: {soma_valores / total:.2f}")
        print("Item mais valioso:", item_mais_valioso)
        print("Maior valor:", maior_valor)
