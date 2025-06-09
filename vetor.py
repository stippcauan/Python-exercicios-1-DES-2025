import random

frutas = ["maçã","banana", "laranja", "uva", "manga"]

print("lista de frutas:")
for i in range (len(frutas)):
    print(f"{i + 1} - {frutas[i]}")

posicao_sorteada = random.randint(1 , 5)

palpite = input("Qual fruta você acha que está na posição sorteada")

fruta_certa = frutas[posicao_sorteada - 1]

if palpite.capitalize() == fruta_certa:
    print("parabens!você acertou!")
    print(f"a fruta na posição{posicao_sorteada} era realmente {fruta_certa}.")
else:
    print("que pena, você errou.")
    print(f"a fruta na posição {posicao_sorteada} era {fruta_certa}.")