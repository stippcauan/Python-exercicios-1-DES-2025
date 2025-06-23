#Loja oferece os seguintes descontos:

#Compras acima de R$ 500,00 têm 10%
#Acima de R$ 300,00 têm 5%
#Menor ou igual a R$ 300,00 não têm desconto

compra = int(input("Digite o valor da compra"))

if compra >500:
    print("Voceê ganhou 10% de desconto.")
elif compra >300:
    print("Você ganhou 5% de desconto.")
else:
    print("Você não conseguiu ganhar desconto.")
    #finalizado