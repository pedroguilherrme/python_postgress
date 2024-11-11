import streamlit as st;
import produto


def Delete():
    st.title('Deletar Produto')
    with st.form(key="Delete_produto"):
        input_id = st.text_input(label="Insira o id do produto que deseja excluir:")
        input_button_submit = st.form_submit_button("Deletar")
    
    if input_button_submit:
        if not input_id:
            st.error('Campos Id não pode ser nulo!!')
        else:
            produto.idproduto = input_id
            produto.delete_produto(produto.idproduto)
            st.success('Produto excluido com sucesso.')
