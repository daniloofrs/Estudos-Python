import time
nome = input("Me diga o seu nome: ")
time.sleep(2)
idade = int(input (f"Que legal {nome}, me diga sua idade: "))
time.sleep(2)
cidade = input(f"sua idade é {idade}, agora, me diga sua cidade: ")
idade_5anos = (idade + 5)
print (f"Seu nome é {nome}, sua idade é {idade}, e sua cidade é {cidade}, e daqui a 5 anos você terá {idade_5anos} anos")

