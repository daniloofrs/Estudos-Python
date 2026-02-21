
import os
import time


titulo = "\033[1mSeja bem-vindo ao calculador de descontos!\033[0m"
print(titulo.center(80))
operador = input("Digite o seu nome: ").capitalize()
time.sleep(1)
print()
print(f"Seja bem vindo, operador(a) {operador}.")
time.sleep(0.5)
input(f"Aperte ENTER para continuar:")

mensalidade = 600.00

lista_premium = []   #alunos que ganharam 30% de desconto.

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    aluno = input("Digite o nome do aluno:")
    if aluno.lower() == "sair":
            print("Saindo do loop...")
            time.sleep(1)
            input("Aperte ENTER para sair.")
            break
    print (f"Aluno(a) {aluno} selecionado.")
    time.sleep(1)
    notas = (input("Digite a nota do aluno: "))
    if notas.lower() == "sair":
        print("Saindo do loop...")
        time.sleep(1)
        input("Aperte ENTER para sair.")
        break
    elif (notas.isdigit()) == False:
        print("Aluno inválido! ")
        time.sleep(1)
        continue
    faltas = (input("Digite as faltas do aluno: "))
    if faltas.lower() == "sair":
        print("Saindo do loop...")
        time.sleep(1)
        input("Aperte ENTER para sair.")
        break

    notas = float(notas)
    faltas = int(faltas)

    if notas >= 9.0 and faltas < 5 and notas <= 10 and faltas >= 0:
        mensalidade_final30 = (mensalidade * (70 / 100))
        time.sleep(1)
        print(f"O aluno {aluno} ganhou 30% de desconto e sua mensalidade ficou com R$:{mensalidade_final30:.2f}")
        lista_premium.append(aluno)
        

    elif (notas >= 7.0 and notas <= 10) or (faltas < 5 and notas > 3.0):
        mensalidade_final10 = (mensalidade * (90 / 100))
        time.sleep(1)
        print(f"O aluno {aluno} ganhou 10% de desconto e sua mensalidade ficou com R$:{mensalidade_final10:.2f}")

    elif notas >= 0 and faltas >= 0:
        time.sleep(1)
        print(f"O aluno {aluno} não ganhou nenhum desconto.")
    
    else: 
        time.sleep(0.8)
        print("Nota do aluno inválida! Tente novamente.")
        continue
    
    input("Aperte ENTER para continuar: ")


print(f"Os alunos contemplados com 30% de desconto são:")
if len(lista_premium) > 0:
    print(f"Total de alunos Premium: {len(lista_premium)}")
    for nome in lista_premium:
        print(f"- {nome}")
else:
    print("Nenhum aluno atingiu os requisitos para o desconto de 30%.")

input ("Aperte Enter para sair: ")

