import streamlit as st;
import produto
import pandas as pd


def Consultar():
    costumeList = []

    for item in produto.todos_produtos():
        costumeList.append([item[0],item[1], item[2]])
    
    df = pd.DataFrame(
        costumeList,
        columns=('Id','Nome', 'Valor')
    )

    st.table(df)