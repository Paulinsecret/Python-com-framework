n1 = float(input("Nota1:"))
n2 = float(input("Nota2:"))

media = (n1+n2)/2

if media > 7:
    print("Você passou!!!")
    situação = 1
else:
    print("Recuperação")
    situação = 2

if situação == 2:
    nota_recuperacao = float(input("Qual a nota de recuperação: "))
    nota_final = (media + nota_recuperacao)/2
    if nota_final >= 5:
        print("Você passou! Ufa!")
    else:
        print("Repitiu mané")
