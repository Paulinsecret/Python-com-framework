aluno1 = input('Nome do aluno: ')

nota_aluno = float(input('Nota do aluno:'))

if nota_aluno >=9:
    print("Excelente")
elif nota_aluno >= 7 and nota_aluno <9:
    print("Bom")
elif nota_aluno >= 5 and nota_aluno < 7:
    print("Regular")
if nota_aluno < 5:
    print("Insuficiente")
    