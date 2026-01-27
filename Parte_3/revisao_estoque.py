itens = ["mouse","fone","mouse","carregador","mouse"]



while True:
    quantidade = 0
    procurar_item = input("Digite um objeto para procurar no estoque: ")

    if procurar_item in itens:
        print ("Objeto encontrado no estoque!")
    elif procurar_item == "sair":
        print ("Saindo do estoque... ")
        break
    else:
        print ("Desculpe, não temos esse item.")
        break

    for objeto in itens:
        if objeto == procurar_item:
            quantidade = quantidade + 1
    print (f"Existem {quantidade} unidades de {procurar_item} no estoque.")



    
