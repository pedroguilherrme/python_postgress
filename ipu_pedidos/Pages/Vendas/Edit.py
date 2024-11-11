import streamlit as st;
import vendas

def Editar():
    st.title('Alterar Venda')
    with st.form(key="Editar_venda"):
        input_value = st.text_input(label="Insira o novo valor da venda:")
        input_id = st.text_input(label="Insira o id da venda que você deseja alterar")

        input_button_submit = st.form_submit_button("Editar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            vendas.valor = input_value
            vendas.idvenda = input_id
            vendas.update_vendas(vendas.valor,vendas.idvenda)
            st.success('Venda atualizado com sucesso.')