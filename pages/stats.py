import streamlit as st
import pandas as pd

st.markdown("# Stats logs")

df2 = pd.read_csv("Maths.csv")
df2 = df2[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
df_new = df2.assign(alcoeveryday=lambda x: (x.Dalc + x.Walc) / 2)
df3 = df_new[df_new['Pstatus'] == 'A'].copy()
df4 = df_new[df_new['Pstatus'] == 'T'].copy()
df5 = df_new[df_new['guardian'] == 'mother']
df6 = df_new[df_new['guardian'] == 'father']
st.write('Below you can choose statistics for each DataFrame.')
st.write('There are DataFrames about kids living in full families, apart families, with mother or with father.')
option = st.selectbox("click to select  ", (['all', 'full', 'apart', 'mother', 'father']))
if option == 'all':
    st.write('DataFrame statistics with all values.')
    st.write(df_new.describe())
if option == 'full':
    st.write('DataFrame statistics with values about kids living in full families.')
    st.write(df4.describe())
if option == 'apart':
    st.write('DataFrame statistics with values about kids living in apart families.')
    st.write(df3.describe())
if option == 'mother':
    st.write('DataFrame statistics with values about kids living with mother.')
    st.write(df5.describe())
if option == 'father':
    st.write('DataFrame statistics with values about kids living with father.')
    st.write(df6.describe())
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
if st.sidebar.checkbox("Support developer"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')

st.write("[Jupyter notebook](https://www.youtube.com/watch?v=dQw4w9WgXcQ)")
st.write()