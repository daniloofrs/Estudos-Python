pecas = ["Ram", "Ssd", "Cpu"]
estoque = [10, 5, 2]




while True:
    entrada = input("Digite o  nome da peça: ").capitalize()
    if entrada in pecas:
        posicao = pecas.index(entrada)
        if estoque[posicao] > 0:
            estoque[posicao] = estoque[posicao] - 1
            print(f"Lista de estoque: - {estoque}")
        elif estoque[posicao] <= 0:
            print ("Peça esgotada. ")
    elif entrada == "sair":
        break

    else:
        print("Peça inválida. ")
    
       

   

