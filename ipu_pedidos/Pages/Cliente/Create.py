import streamlit as st;
import cliente


def Create():
    st.title("Incluir Cliente")
    with st.form(key="Include_cliente"):
        input_name = st.text_input(label="Insira seu nome:")
        input_cpf = st.text_input(label="Insira seu CPF:")
        input_gender = st.selectbox(label="Insira seu gênero:", options=["M","F"])
        input_button_submit = st.form_submit_button("Cadastrar")

    if input_button_submit:
        if not input_name or not input_cpf:
            st.error('Campos Nome e CPF, não podem ser nulos!!')
        else:
            cliente.nome = input_name
            cliente.cpf = input_cpf
            cliente.genero = input_gender

            cliente.insert_cliente(cliente.nome,cliente.cpf,cliente.genero)
            st.success("Cliente inserido com sucesso.")