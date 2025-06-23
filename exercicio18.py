#Receba duas notas e seus respectivos pesos. Calcule a média ponderada.
#Fórmula: (nota1 × peso1 + nota2 × peso2) / (peso1 + peso2)

nota1 = float(input("Digite sua primeira nota.")) 
nota2 = float(input("Digite sua segunda nota."))

peso1 = 10
peso2 = 10

resultado = nota1 * peso1 / 10 + nota2 * peso2 / 10
print(resultado)

if resultado >= 120:
    print("Parabéns! você passou!")
else:
    print("Você não passou!")
#finalizado