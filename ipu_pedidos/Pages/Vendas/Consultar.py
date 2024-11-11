import streamlit as st;
import vendas
import pandas as pd

def Consultar():
    costumeList = []

    for item in vendas.todas_vendas():
        costumeList.append([item[0],item[1], item[2],item[3],item[4]])
    
    df = pd.DataFrame(
        costumeList,
        columns=('Id_Venda','Nome Funcionário', 'Produto','Valor','Data')
    )

    st.table(df)