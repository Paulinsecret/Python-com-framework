# import streamlit as st

# import pandas as pd

# import datetime as dt
# # st.title('hello world')

# # st.write("Hello world")

# # st.text_input("Escreva aqui:")

# # st.map()



# # dados  =  {
# # 'Dia': ['Jan','Fev','Mar'],
# # 'Vendas':[5000.0,1000.0,9000.0]
# # }




# # df =  pd.DataFrame(dados)


# # if st.button('Gerar Grafico'):
# #     st.bar_chart(df.set_index('Dia'))




# # df2 =  pd.read_csv('vendas.csv')


# # if st.button('Gerar grafico'):
# #     st.bar_chart(df2, x = 'vendedor', y = 'venda')
# #     st.table(df2)


# import streamlit as st
# from abc import ABC, abstractmethod
# import datetime


# st.set_page_config(page_title='POO e Streamlit')
# st.title('Laboratório de testes')


# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo =  titulo
#         self.autor = autor
#         self.ano = ano
#         self.lista  = []
    
#     def cadastro_livro(self):
#         self.lista.extend([self.titulo, self.autor, self.ano])
#         return self.lista
#     def __str__(self):
#         st.write(self.lista)
#         print(self.lista)

# nome  = st.text_input('Digite o nome do livro')
# autor = st.text_input('Digite o nome do autor')
# ano = st.date_input('Selecione o ano')

# if st.button('Criar.csv'):
#     l = Livro(nome, autor, ano)
#     dados = l.cadastro_livro()
#     df = pd.DataFrame(dados)
#     df.to_csv('dados1.csv')


# l = Livro(nome, autor, ano)
# l.cadastro_livro()





# if st.button('Salvar na lista'):


#     st.success('Dado cadastrado') 
# l.__str__()

