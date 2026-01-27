import time 

produtos_disponiveis = ["Pão", "Leite","café"]

precos_disponiveis = [1.50, 4.00, 15.00]

carrinho = []

while True:
    desejo = input("Digite o nome do produto que você deseja comprar: ")
    if desejo == "fim":
        print ("Saindo do carrinho...")
        time.sleep(1)
        input ("Finalizado. Pressione qualquer tecla para sair.")
        break
    if desejo in produtos_disponiveis:
            posicao = produtos_disponiveis.index(desejo)
            preco = precos_disponiveis[posicao]
            carrinho.append(preco)
            print(f"Adicionado: {desejo} - R${preco:.2f}")
    else:
        print("Procurando produto... ")
        time.sleep(1)
        print("Produto não encontrado.")

print (f"O total da compra foi: R$:{sum(carrinho):.2f}")
print (f"Itens comprados: {len(carrinho)}")


    
