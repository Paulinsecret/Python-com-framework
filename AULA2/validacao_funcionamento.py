


dia = int(input("Qual o dia da semana que deseja ver disponibilidade:" ))

hora = int(input("Qual hora deseja ver: "))

verificacao = (hora > 8 and hora <19) and (dia > 0 and dia < 6) and 'Está aberto' or 'Está fechado'

print(verificacao)


# check_dia = (dia == 'segunda' or 'terca' or 'quarta' or 'quinta' or 'sexta') and 'disponivel' or 'indisponivel'

# check_hora = (hora == 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 ) and 'aberto' or 'fechado'


# final = (check_dia == 'disponivel' and check_hora == 'aberto') and 'O local está aberto nessa data e horário' or 'O local esta fechado nessa data e horário'

# print(final)


