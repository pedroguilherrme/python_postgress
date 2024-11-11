import streamlit as st;
import cliente
import pandas as pd

def Consultar():
    costumeList = []

    for item in cliente.todos_clientes():
        costumeList.append([item[0],item[1], item[2],item[3]])
    
    df = pd.DataFrame(
        costumeList,
        columns=('Id','Nome', 'CPF','Gênero')
    )

    st.table(df)