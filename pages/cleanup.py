import streamlit as st
import pandas as pd

st.markdown("# Cleanup logs️")
st.write('I checked the tabular values for defects and each line for consistency with its class. The result can be seen below.')
df2 = pd.read_csv("Maths.csv")
df2 = df2[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
tmp = len(df2)
df2.dropna()
fl = True
if len(df2) == tmp:
    st.write("No NaN fields detected")
else:
    st.write("Cleaned up NaN values, dropped {0} rows".format(tmp - len(df2)))
for i in ["famsize", "Pstatus", "guardian", "romantic"]:
    if df2[i].dtypes != "object":
        st.write("wrong data type in column {0}, must be object".format(i))
        fl = False
for i in ["goout", "Dalc", "Walc"]:
    if df2[i].dtypes != "int64":
        st.write("wrong data type in column price, must be int64")
        fl = False

if fl:
    st.write("all data types are correct")
st.write("cleanup complete")
if st.sidebar.checkbox("Support developer "):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')
