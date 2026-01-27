import time

notas = []

while True:
    entrada = (input("Digite a nota do aluno: "))
    if entrada == "sair":
        print ("Saindo...")
        time.sleep(1)
        break
    nota_convertida = float(entrada)
    notas.append(nota_convertida)


calculo = sum (notas)/ len (notas)

if calculo >= 7:
    print ("Aluno aprovado! ")

if calculo >= 5 and calculo < 7:
    print ("Aluno em recuperação! ")

if calculo < 5:
    print (" Aluno Reprovado!")
