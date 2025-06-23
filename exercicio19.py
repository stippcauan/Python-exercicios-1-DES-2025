#Peça três números e exiba-os em ordem crescente.]

n1 = float(input("Digite o primeiro numero."))
n2 = float(input("Digite o segundo numero."))
n3 = float(input("Digite o terceiro numero"))

numeros = [n1, n2, n3]
numeros.sort()

print("numeros em ordem crescente:")
for numero in numeros:
    print(numero)
    