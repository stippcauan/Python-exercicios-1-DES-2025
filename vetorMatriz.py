alunos = ["Alice", "bruno", "carla", "diego", "cauan"]

dias = ["seg", "ter", "qua", "qui"]

reservas = [["ausente" for _ in dias] for _ in alunos]

print("preencha com 'X' para ausência:")

for i, aluno in enumerate(alunos):
    print(f"\naluno: {aluno}") 
    for j, dia in enumerate(dias):
        entrada = input(f" {dia}:")
        if entrada.upper() == 'S':
            reservas[i] [j] = "presentes"

print("\ntabela de reservas:")
print(f"{'aluno':<10}{' '.join([f'{d:<10}' for d in dias]) }")
for i, aluno in enumerate(alunos):
    print(f"{aluno:<10} {' '.join([f'{res:<10}' for res in reservas[i]])}")