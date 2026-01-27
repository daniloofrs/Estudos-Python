nomes = []

for i in range(1, 4):
    pessoas = input("Digite um nome: ")
    nomes.append(pessoas)

print(*f"Os nomes são: {nomes}")