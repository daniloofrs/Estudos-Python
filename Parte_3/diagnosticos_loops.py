x = 10
while x > 0:
    print(x)
    x = x - 1
# Faltava apenas colocar uma linha de código: x = x - 1, obrigando o código à diminuir.

# Era só trocar o n por total dentro das chaves do print. 
# O erro acontecia porque o n guardava apenas o último item da lista, 
# enquanto o total acumulava a soma de todos eles.
notas = [7, 8, 10]
total = 0

for n in notas:
    total = total + n

print(f"A soma é {total}")



# Eu quero que o computador conte de 1 até 5 (1, 2, 3, 4, 5)
for i in range(1, 6, +1):
    print(i)

    # Essa foi fácil, pensei que era só trocar os sinais de "-" para "+" 
    # mas na verdade eu tinha que escrever o range inteiro
