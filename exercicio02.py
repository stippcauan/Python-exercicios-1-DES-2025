#  Juliana está coordenando entregas de projetos e precisa calcular o tempo total necessário 
# para finalizar três tarefas: X, Y e Z.
#  Se alguma tarefa estiver com o tempo de entrega negativo, deve-se exibir uma mensagem de 
# erro e não somar o total.

dia_01 = int(input("Dias para atividade 01 = "))
dia_02 = int(input("Dias para atividade 02 = "))
dia_03 = int(input("Dias para atividade 03 = "))

soma = dia_01 + dia_02 + dia_03

if dia_01<0 or dia_02<0 or dia_03<0:
   print("erro nnumero negaivo")
else:
   soma = dia_01 + dia_02 + dia_03
   print(f"tempo total do projeto: {soma} dias")
