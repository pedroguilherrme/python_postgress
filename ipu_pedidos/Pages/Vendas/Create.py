import streamlit as st;
import vendas

def create_vendas():
    st.title("Incluir Vendas")
    with st.form(key="Include_venda"):
        input_id_funcionario = st.text_input(label="Insira id do funcionário")
        input_value = st.text_input(label="Insira seu Valor:")
        input_id_produto = st.text_input(label="Insira o Id do produto:")
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_button_submit:
        if not input_id_funcionario or not input_id_produto:
            st.error('Campos Ids, não podem ser nulos!!')
        else:
            vendas.idfuncionario = input_id_funcionario
            vendas.valor = input_value
            vendas.idproduto = input_id_produto

            vendas.insert_venda(vendas.idfuncionario,vendas.valor,vendas.idproduto)
            st.success("Venda inserida com sucesso.")