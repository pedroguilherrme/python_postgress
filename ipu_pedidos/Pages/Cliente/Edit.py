import streamlit as st;
import cliente

def Editar():
    st.title('Alterar Cliente')
    with st.form(key="Editar_cliente"):
        input_name = st.text_input(label="Insira o novo nome do cliente:")
        input_id = st.text_input(label="Insira o id do cliente que você deseja alterar")

        input_button_submit = st.form_submit_button("Editar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            cliente.nome = input_name
            cliente.idcliente = input_id
            cliente.update_cliente_nome(cliente.nome,cliente.idcliente)
            st.success('Cliente atualizado com sucesso.')