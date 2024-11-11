import streamlit as st;
import funcionario
import pandas as pd


def Consultar():
    costumeList = []

    for item in funcionario.todos_funcionarios():
        costumeList.append([item[0],item[1], item[2]])
    
    df = pd.DataFrame(
        costumeList,
        columns=('Id','Nome', 'CPF')
    )

    st.table(df)