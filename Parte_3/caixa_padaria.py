precos = []


while True:
    preco_produto = float(input("Digite o preço do produto: "))

    if preco_produto < 0:
        print ("Valor inválido, digite um número maior que 0. ")  

    if preco_produto == 0:
        break
    if preco_produto > 0:
        precos.append(preco_produto)


total = 0 

for valor in precos:
    total =  total + valor
print (f"O valor total da compra é: R${total:.2f}")
print (f"A média por produto foi: {total/len(precos):.2f}")