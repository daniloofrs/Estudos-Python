Convidados = []


while True:
    Convidado = input("Digite um nome de convidado ou a palavra sair: ")

    if Convidado == "sair":
        break
    Convidados.append(Convidado)
    print(f"Convidado(a) {Convidado} adicionado.")
    
print(f"O total de convidados é {len(Convidados)}")
for pessoa in Convidados:
    print(f"- {pessoa}")
