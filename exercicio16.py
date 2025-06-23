#Crie um programa que calcule o reajuste de salário:

#Salários até R$ 2000,00: +15%
#De R$ 2000,01 a R$ 5000,00: +10%
#Acima de R$ 5000,00: +5%

salario = float(input("Digite seu salario."))

if salario <= 2000:
    print("Você teve 15% a mais.")
elif salario >= 2000.01 <= 5000.01:
    print("Você teve 10% a mais")
else:
    print("Você teve 5% a mais.")
    