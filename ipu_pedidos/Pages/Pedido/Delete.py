import streamlit as st;
import pedidos

def Delete():
    st.title('Deletar Pedido')
    with st.form(key="Delete_pedido"):
        input_id = st.text_input(label="Insira o id do pedido que deseja excluir:")
        input_button_submit = st.form_submit_button("Deletar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            pedidos.id = input_id
            pedidos.delete_pedido(pedidos.id)
            st.success('Pedido excluido com sucesso.')
