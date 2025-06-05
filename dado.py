import random

input("Pressione o enter para lançar o dado")

resultado = random . randint(1,6)

print(f"O dado rolou: {resultado}")

if resultado == 6:
    print("ual! você é fera")

elif resultado <=2:
    print("Você tirou nota baixa.")
else:
    print("Sua nota foi intermediaria")