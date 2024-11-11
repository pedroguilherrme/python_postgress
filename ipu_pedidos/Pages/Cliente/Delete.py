import streamlit as st;
import cliente


def Delete():
    st.title('Excluir Cliente')
    with st.form(key="Delete_cliente"):
        input_id = st.text_input(label="Insira o id do cliente que deseja excluir:")
        input_button_submit = st.form_submit_button("Deletar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            cliente.idcliente = input_id
            cliente.delete_cliente(cliente.idcliente)
            st.success('Cliente excluido com sucesso.')
