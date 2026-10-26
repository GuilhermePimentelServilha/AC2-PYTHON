import json

def definir_nivel(valor):
    if valor < 50:
        return "Necessita Substituição"
    elif valor < 80:
        return "Regular"
    return "Excelente Estado"

def buscar_equipamento_json():
    nome_busca = input("Digite o nome do equipamento: ")

    try:
        with open("equipamentos.json", "r", encoding="utf-8") as arquivo_json:
            lista = json.load(arquivo_json)
    except:
        return

    encontrado = False
    for item in lista:
        if item["nome"].lower() == nome_busca.lower():
            print("Nome:", item["nome"])
            print("Patrimônio:", item["idade"])
            print("Valor:", item["pontuacao"])
            print("Estado de Conservação:", definir_nivel(item["pontuacao"]))
            encontrado = True
            break

    if not encontrado:
        print("Equipamento não localizado.")
