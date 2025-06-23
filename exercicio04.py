# Isabela está desenvolvendo um aplicativo de corrida que calcula a velocidade média do usuário.
# O programa deve receber a distância percorrida e o tempo gasto, calcular a velocidade e indicar se foi 
# lenta (<5 km/h), moderada (5 a 10 km/h) ou rápida (>10 km/h).

distancia = float(input("Digite o tempo"))
tempo = float(input("Digite o tempo"))

V_media = distancia /tempo

if V_media<5:
    print("lento")

elif V_media >=5 <= 10:
    print("moderado")

else:
    print("reprovado")
    #finalizado

