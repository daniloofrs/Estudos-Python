soma_total = 0
for x in range (4):
    nota = float(input("Digite a nota da matéria: "))
    soma_total = (nota + soma_total)
print (f"A soma total das notas é: {soma_total:.2f}")