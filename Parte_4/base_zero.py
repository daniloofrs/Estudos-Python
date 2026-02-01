pergunta = int(input("Digite a idade do usuário: "))

if pergunta >= 18:
    print("Acesso Liberado!")
elif pergunta > 0:
    print("Acesso negado!")
else:
    print("Idade inválida")
    
