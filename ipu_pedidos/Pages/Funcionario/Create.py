import streamlit as st;
import funcionario


def Create():
    st.title("Incluir Funcionario")
    with st.form(key="Include_funcionario"):
        input_name = st.text_input(label="Insira o nome do funcionario:")
        input_cpf = st.text_input(label="Insira seu CPF:")
        input_button_submit = st.form_submit_button("Incluir")

    if input_button_submit:
        if not input_name or not input_cpf:
            st.error('Campos Nome e CPF, não podem ser nulos!!')
        else:
            funcionario.nome = input_name
            funcionario.cpf = input_cpf
            

            funcionario.insert_funcionario(funcionario.nome,funcionario.cpf)
            st.success("Funcionario inserido com sucesso.")