# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.

umidade = int(input("Digite a umidade local"))
if umidade >=70:
    print("Alerta umidade utrapassou 70")
else:
    print("Umidade dentro do padrão")
       

