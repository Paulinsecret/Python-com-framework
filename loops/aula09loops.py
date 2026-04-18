
""" sequencia = []



for i in range(5):
    print(i)

contador = 0
while contador < 5:
    contador  = contador + 1
    print(contador) """


#e-commerce

dados = {
    'login': '@pau',
    'senha': '1234',
    'carrinho': ['A', 'B', 'C', 'D'],
    'total': [100.50, 250.55, 4000.00, 10000.00 ]    
}
 

for x in range(3):
    senha = input("Senha:")
    login = input("Login:")

    if senha == dados ['senha'] and login == dados['login']:
        print('Seja bem vindo(a)')
        pergunta = input("Deseja comprar? s/n")
        while pergunta == 's':
            produto = int(input("Escolha o produto:"))
            dados['carrinho'].append(dados['produtos'][produto])
            dados['total'].append(dados['valores'][produto])
            print(dados['carrinho'])
            print(dados['total'])
            print('R$', sum(dados['total']))
            pergunta = input("Deseja continuar comprando? s/n")
        else: 
            print('Forma de pagamento')
            pag = ['px', 'debito', 'credito']

            print(pag[int(input('Escolha'))])
    else:
        print('Tente novamente')
else: 
    print("Senha bloqueada")