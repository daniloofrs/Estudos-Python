salário = float (input ("Digite seu salário:"))

if salário <= 3000:
    print ("Programador Júnior")
elif salário > 3000 and salário <= 6000:
    print ("Você é um Programador Pleno")
elif salário > 6000 and salário <= 15000:
    print ("Programador Sênior")
else:
    print("Diretor de Projetos")