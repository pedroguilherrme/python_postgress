import streamlit as st;
import vendas


def Delete():
    st.title('Excluir Venda')
    with st.form(key="Delete_venda"):
        input_id = st.text_input(label="Insira o id da venda que deseja excluir:")
        input_button_submit = st.form_submit_button("Deletar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            vendas.idvenda = input_id
            vendas.delete_venda(vendas.idvenda)
            st.success('Venda excluida com sucesso.')
