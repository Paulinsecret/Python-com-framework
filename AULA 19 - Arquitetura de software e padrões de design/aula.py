import streamlit as st
import controller

nova_entrada = st.text_input('escreva algo ...')

if st.button('salvar'):
    if controller.adicionar_nota(nova_entrada):
        st.success('salva com sucesso')
    else:
        st.error('digite algo antes de salvar')

st.subheader('histórico')
for nota in controller.listar_notas():
    st.write(nota[0])

