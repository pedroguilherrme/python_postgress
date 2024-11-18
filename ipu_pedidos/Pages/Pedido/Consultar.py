import streamlit as st;
import pedidos
import pandas as pd

def Consultar():
    costumeList = []

    for item in pedidos.todos_pedidos():
        costumeList.append([item[0],item[1], item[2],item[3]])
    
    df = pd.DataFrame(
        costumeList,
        columns=('IdPedido','Nome do Produto', 'Nome do Cliente', 'Data')
    )

    st.table(df)
