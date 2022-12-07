import streamlit as st
import pandas as pd

st.markdown("# Stats logs️")
st.write('50% - mediana')
df2 = pd.read_csv("Maths.csv")
df2 = df2[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
st.write(df2.describe())


@st.cache
def convert_df(df):
    return df.to_csv().encode('utf-8')


csv = convert_df(df2)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Maths.csv',
    mime='text/csv',
)
if st.sidebar.checkbox("Поддержать разработчика"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')

st.write("[Jupyter notebook](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")