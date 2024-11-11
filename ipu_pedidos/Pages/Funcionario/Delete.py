import streamlit as st;
import funcionario

def Delete():
    st.title('Deletar Funcionario')
    with st.form(key="Delete_funcionario"):
        input_id = st.text_input(label="Insira o id do funcionario que deseja excluir:")
        input_button_submit = st.form_submit_button("Deletar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            funcionario.idfuncionario = input_id
            funcionario.delete_funcionario(funcionario.idfuncionario)
            st.success('Produto excluido com sucesso.')
