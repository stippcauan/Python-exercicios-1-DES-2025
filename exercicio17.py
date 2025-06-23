#Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.
#Fórmula: F = C × 1.8 + 32

c = float(input("digite a temperatura em celsius:"))
f = c * 1.8 + 32
print(f"a temperatura em fahrenheit é: {f:.2f}°f")