import time
valor_investimentos = float(input("Bem vindo ao Calculador de Investimentos Simples, por favor, me diga o valor inicial que você deseja investir: "))
time.sleep(1)
taxa_rendimento_anual = float(input("Me diga a taxa de rendimento anual: "))
valorfinal = (valor_investimentos + (valor_investimentos * taxa_rendimento_anual / 100))
print (f"O Valor final dos seus invesimentos após um ano é de {valorfinal:.2f}")