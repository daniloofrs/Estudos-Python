equipe = []
while True:
 entrada_dados = input("Digite um nome: ")
 if entrada_dados == "fim":
    break
 else: equipe.append(entrada_dados)
for total_equipe in equipe:
 print (f"Total de pessoas:{total_equipe}")