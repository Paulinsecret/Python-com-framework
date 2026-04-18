sexo = int(input("Sexo M/F:")) 

nascimento = int(input("Ano de nascimento:"))   

deficiencia = input("Possui deficiência S/N:")


if sexo == 'f':
    print('Não obrigatório')
elif sexo =='m':
    idade = 2026 - nascimento 
    if deficiencia == 'S':
        print('Não pode se alistar')
    if idade == 18 and deficiencia== 'n':
        print("Alistamento imediato")
    elif idade >=18 and idade >=45:
        print("Passou do prazo")
    else:
        print("Não tem idade")
    