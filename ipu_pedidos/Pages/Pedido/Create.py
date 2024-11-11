import streamlit as st;
import pedidos


def Create():
    st.title("Incluir Pedido")
    with st.form(key="Include_pedido"):
        input_name_cliente = st.text_input(label="Insira o nome do Cliente")
        input_name = st.text_input(label="Insira o nome do Produto:")
        input_button_submit = st.form_submit_button("Incluir")

    if input_button_submit:
        if not input_name or not input_name_cliente:
            st.error('Campo Nome, não podem ser nulo!!')
        else:
            pedidos.nome_produto = input_name
            pedidos.nome_cliente = input_name_cliente
            

            pedidos.insert_pedido(pedidos.nome_produto,pedidos.nome_cliente)
            st.success("Produto inserido com sucesso.")