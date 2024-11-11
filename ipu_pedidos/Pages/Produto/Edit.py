import streamlit as st;
from os import write
import produto
import pandas as pd
import Controller.ClienteController as ClienteController

def Editar():
    st.title('Alterar Produto')
    with st.form(key="Editar_produto"):
        input_value = st.text_input(label="Insira o novo valor do produto:")
        input_id = st.text_input(label="Insira o id do produto que você deseja alterar")

        input_button_submit = st.form_submit_button("Editar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            produto.valor = input_value
            produto.idproduto = input_id
            produto.update_produto(produto.valor,produto.idproduto)
            st.success('Produto atualizado com sucesso.')