colegas = ["Ana","Bruno","Caio","Isabela","Eliane"]
novo_amigo = input ("Digite um nome de um nova pessoa: ")
colegas.append(novo_amigo)
for colega in colegas:
    print(f"O aluno {colega} está presente na aula de hoje.")