#Peça ao usuário uma senha e verifique se ela contém pelo menos 8 caracteres.
#Exiba uma mensagem de "Senha válida" ou "Senha muito curta".

senha = int(input("Digite a sua senha."))
digitos = len(senha)

if senha >= 8:
    print("senha correta.")
else:
    print("Senha incoreta.")
    #finalizado