produtos = ["Teclado", "Mouse", "Monitor"]

precos = [150.00, 80.00, 900.00]

entrada = input("Digite um nome de um produto: ").capitalize()

if entrada in produtos:
    posicao = produtos.index(entrada)
    valor = precos[posicao]
    print (f"O {entrada} custa R$:{valor:.2f}")
else:
    print("Produto não encontrado. ")

