import os
import time


titulo = "\033[1mSeja bem-vindo ao coletor de dados!\033[0m"
print(titulo.center(80))
operador = input("Digite o seu nome: ").capitalize()
time.sleep(1)
print()
print(f"Seja bem vindo, operador(a) {operador}.")
time.sleep(0.5)
input(f"Aperte ENTER para continuar:")


while True:
    def limpar_tela():
        os.system('cls' if os.name == 'nt' else 'clear')
    limpar_tela()
    nome_aluno = input("Digite o nome do aluno: ").capitalize()


    time.sleep(0.5)
    if nome_aluno.lower() == "sair":
        print("Saindo do coletor de dados...")
        time.sleep(1)
        input("Aperte ENTER para sair. ")
        break
    else:
        print(f"O aluno {nome_aluno} foi selecionado. ")
    time.sleep(1)

    ano_ingresso = input("Digite o ano que o aluno ingressou: ")

    if ano_ingresso.lower() == "sair":
        print("Saindo do coletor de dados...")
        time.sleep(1)
        input("Aperte ENTER para sair. ")
        break
    elif (ano_ingresso.isdigit()) == False:
        print("Ano inválido. Por favor, tente novamente.")
        time.sleep(1)
        continue
    elif int(ano_ingresso) > 2026 or int(ano_ingresso) < 1970:
        time.sleep(1)
        print("Ano inválido. Por favor, tente novamente.")
        time.sleep(1)
        continue

    elif (ano_ingresso.isdigit()) == True:
        final = 2026 - int(ano_ingresso)
        if final == 0:
            print ("O aluno é um calouro e ingressou este ano!")
        elif final == 1:
            print ("O aluno está no seu segundo ano (1 ano completo).")
        else:   
            print (f"O {nome_aluno} está a {final} anos na universidade. ")
        time.sleep(0.5)
        input(f"Aperte ENTER para continuar, {operador}")
        time.sleep(0.5)

    elif (ano_ingresso.isdigit()) == False:
        print("Ano inválido.")
        time.sleep(1)
        continue

    else:
        print("Ano inválido. Por favor, tente novamente.")
        continue

print(f"Coletor de dados descontinuado, até mais, {operador}.")
