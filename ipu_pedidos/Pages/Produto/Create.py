import streamlit as st;
import produto


def Create():
    st.title("Incluir Produto")
    with st.form(key="Include_produto"):
        input_name = st.text_input(label="Insira o nome do produto:")
        input_value = st.text_input(label="Insira seu valor:")
        input_button_submit = st.form_submit_button("Incluir")

    if input_button_submit:
        if not input_name or not input_value:
            st.error('Campos Nome e Valor, não podem ser nulos!!')
        else:
            produto.nome = input_name
            produto.valor = input_value
            

            produto.insert_produto(produto.nome,produto.valor)
            st.success("Produto inserido com sucesso.")