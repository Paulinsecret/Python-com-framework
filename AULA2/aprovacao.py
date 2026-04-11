matematica = float(input("Nota de matemática:"))

portugues = float(input("Nota de portugues:"))


nota_final = matematica >= 6 and portugues >= 6 and 'Foi aprovado' or 'Foi reprovado'


print(nota_final)