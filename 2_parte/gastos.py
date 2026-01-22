import time 
print ("Olá, bem vindo ao seu controle de gastos, cliente")
time.sleep(1)
almoço = float(input ("Por favor, me diga quanto você gastou no almoço hoje?"))
time.sleep(1)
passagem_onibus = float(input ("Quanto você pagou na passagem de ônibus hoje?"))
time.sleep(1)
internet = float(input ("Quanto foi a sua internet hoje?"))
time.sleep(1)
total = (almoço + passagem_onibus + internet)
print (f"Olá Cliente, o seu gasto total hoje foi de R$:{total}")
if total >50:
    print("Cuidado, você gastou muito hoje!")
else:
    print("Seus gastos estão sob controle.")
