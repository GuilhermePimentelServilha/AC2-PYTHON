from cadastrar_equipamento import cadastrar_equipamento
from historico import ver_historico_txt
from lista import listar_inventario_csv
from busca import buscar_equipamento_json

while True:
    print("\n=== SISTEMA DE INVENTÁRIO DO LABORATÓRIO ===")
    print("1 - Cadastrar equipamento ")
    print("2 - Ver histórico de ocorrencias")
    print("3 - Listar inventário completo e gerar relatório ")
    print("4 - Buscar equipamento detalhado com estado de conservação ")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_equipamento()
    elif opcao == "2":
        ver_historico_txt()
    elif opcao == "3":
        listar_inventario_csv()
    elif opcao == "4":
        buscar_equipamento_json()
    elif opcao == "5":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
