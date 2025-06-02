# Renata quer solicitar um financiamento, mas precisa verificar se cumpre os critérios:

# Salário mensal acima de R$ 3.000,00
# A parcela não pode ser maior que 35% do salário

salario_mensal = float(input("Digite o salário mensal de Renata: "))
parcela_maxima = salario_mensal * 0.35

if salario_mensal > 3000:
    print("Renata tem salário superior a R$ 3.000,00.")
    print(f"A parcela máxima que ela pode ter é: R$ {parcela_maxima:.2f}")
else:
    print("O salário mensal de Renata é inferior a R$ 3.000,00.")
    print("Ela não atende ao critério de salário mínimo.")