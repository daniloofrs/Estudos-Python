import time


while True:
    aluno = input("Digite o nome do aluno: ").capitalize()
    time.sleep(0.5)
    if aluno.lower() == "sair":
        print("Saindo do validador...")
        input("Pressione Enter para sair: ")
        break
    matriculado_pergunta = input("O aluno está matriculado?").capitalize()
    time.sleep(0.5)
    if matriculado_pergunta.lower() == "sair":
        print("Saindo do validador...")
        input("Pressione Enter para sair: ")
        break
    elif matriculado_pergunta.lower() == "sim" or matriculado_pergunta.lower() == "s":
        nota = (input("Digite a nota do aluno: "))
        time.sleep(0.5)
        if nota.lower() == "sair":
                print("Saindo do validador...")
                input("Pressione Enter para sair: ")
                break
        elif float(nota) >= 7.0:
                livrosatrasados = input("O aluno tem mais de 2 livros atrasados? ")
                time.sleep(0.5)
                if livrosatrasados.lower() == "não" or livrosatrasados.lower() == "n":
                    time.sleep(0.5)
                    print("Aprovado!")
                    horas = int(input("Por quantas horas o aluno deseja o notebook?"))
                    if horas >= 5:
                            time.sleep(0.5)
                            print(f"Lembre o aluno(a) {aluno} de levar o carregador!")
                            print(f"Aluno(a) {aluno} aprovado!")
                    else:
                         print(f"Aluno {aluno} aprovado")
                else:
                    print(f"Muitos livros atrasados. Aluno {aluno} reprovado!")
        else:
            print(f"Aluno(a) {aluno} foi reprovado por nota. ")


    elif matriculado_pergunta.lower() == "não" or matriculado_pergunta.lower() == "n":
        print("aluno reprovado!")