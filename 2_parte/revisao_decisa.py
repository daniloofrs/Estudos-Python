velocidade_carro = float(input("Digite a velocidade do carro: "))
if velocidade_carro > 80:
    print ("MULTADO!")
    multa_carro =((velocidade_carro - 80) * 7)
    print (f"A multa foi:{multa_carro:.2f}")
else:
    print ("Boa viagem! Dirija com segurança.")
