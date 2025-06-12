#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = int(input("Digite a sua senha."))

if senha >= 8:
    print("Sua senha está valida.")
else:
    print("Sua senha está invalida.")