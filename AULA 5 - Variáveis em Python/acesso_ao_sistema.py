nome = str(input("Qual o seu nome:"))

senha = int(input("Sua senha:"))


autorizacao = (nome == "admin" and senha == 1234) and 'Acesso autorizado' or 'Acesso negado'

print(autorizacao)