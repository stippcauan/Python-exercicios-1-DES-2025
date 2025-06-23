# Bianca está programando o controle de acesso a uma plataforma que só funciona entre 9h e 21h.
# O programa deve receber a hora atual (formato 24h) e informar se o acesso é permitido.

hora1 = int(input("Digite que horas são"))

if hora1 <9 >21:
   print("Você ainda esta na carga horaria")
else:
   print("Você esta fora da carga horaria")
   #finalizado