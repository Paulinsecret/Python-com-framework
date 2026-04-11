ano = int(input("Insira o ano:"))


bissexto = (ano % 4 == 0 and ano % 400 == 0) and not ano % 100 == 0 and 'É bissexto' or 'Não é bissexto'

print(bissexto)