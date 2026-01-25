import time 
compras = ["Pão","leite","ovos"]
print (*compras)
time.sleep(1)
compras.append(input("Deseja colocar mais algum item? Digite aqui: "))
compras.sort()
for item in compras:
 print (f"- {item}")