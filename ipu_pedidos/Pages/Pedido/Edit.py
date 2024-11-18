import streamlit as st;
import pedidos

def Editar():
    st.title('Alterar Pedido')
    with st.form(key="Editar_pedido"):
        input_id = st.text_input(label="Insira o id do pedido que você deseja alterar")
        input_name = st.text_input(label="Insira o novo produto:")

        input_button_submit = st.form_submit_button("Editar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            pedidos.idpedido = input_id
            pedidos.nome_produto = input_name
            pedidos.update_pedido(pedidos.nome_produto,pedidos.idpedido)
            st.success('Produto atualizado com sucesso.')