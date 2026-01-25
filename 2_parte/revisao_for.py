import time
print ("Seja bem vindo à tabuada interativa!")
time.sleep(1)
nome = int(input("Por favor, digite um número inteiro: "))
time.sleep(1)
for item in range(1,11):
    print(f"{nome} x {item} = {nome * item}")