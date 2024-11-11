import streamlit as st;
import funcionario

def Editar():
    st.title('Alterar Funcionario')
    with st.form(key="Editar_funcionario"):
        input_name = st.text_input(label="Insira o nome:")
        input_id = st.text_input(label="Insira o id do funcionario que você deseja alterar")

        input_button_submit = st.form_submit_button("Editar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            funcionario.nome = input_name
            funcionario.idfuncionario = input_id
            funcionario.update_funcionario(funcionario.nome,funcionario.idfuncionario)
            st.success('Funcionario atualizado com sucesso.')