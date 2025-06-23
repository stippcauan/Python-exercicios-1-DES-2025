# Diego está acompanhando seu consumo de internet mensal, que tem um limite de 100 GB.
# O programa deve receber o total consumido e avisar se ele ultrapassou o limite.

consumo = int(input("digite seu consumo de internet mensal."))

soma = consumo
if consumo < 100 :
    print("Seu consumo mensal foi:" , soma)
elif consumo >100 :
    print("Você ultrapassou seu limite.")
else:
    print("Cuidado, você chegou ao limite")
    #finalizado