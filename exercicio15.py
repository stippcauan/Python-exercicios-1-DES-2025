#Peça a idade do usuário e diga se ele pode se cadastrar em um site:

#Permitido: 13 anos ou mais

idade = int(input("Digite a sua idade."))

if idade >= 13:
    print("Parabéns! você já pode se cadastrar.")
else:
    print("Você ainda não pode se cadastrar.")
    #finalizado    