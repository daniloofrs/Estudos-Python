usuarios_bloqueados = ["admin","teste","root"]

while True:
    usuario = input("Digite um nome de usuário: ")
    if usuario == "sair":
         break
    if usuario in usuarios_bloqueados:
        print ("Acesso negado! Usuário banido.")
    
    else:
        print (f"Bem-vindo, {usuario}! Acesso liberado.")