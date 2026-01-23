import time
notas = []
for i in range(3):
    nota_atual = float(input("Me diga sua nota:"))
    notas.append(nota_atual)
media = sum(notas) / len(notas)
print (f"Sua média final foi: {media: .2f}")
time.sleep(2)
if media >= 7.0:
  print("Parabéns, você foi aprovado")
else:
    print("Você não passou, estude mais na próxima.")
