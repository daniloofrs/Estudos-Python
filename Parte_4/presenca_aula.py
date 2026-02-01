import time

lista = ["Ana","Beto","Caio","Duda"]


while True:
    entrada = input("Digite um nome de um aluno: ").capitalize()
    if entrada == "Sair":
            print("Saindo...")
            time.sleep(1)
            break
    if entrada in lista:
            print(f"Aluno(a) {entrada} já matriculado.")
            continue
    else:
            lista.append(entrada)
    

print (f"Existem {len(lista)} alunos presentes na aula. ")
