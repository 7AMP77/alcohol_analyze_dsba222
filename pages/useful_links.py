import streamlit as st
import pandas as pd

if st.sidebar.checkbox("Support developer"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')
with open("romanbokhyan_projectdsba222.ipynb", "rb") as file:
    st.download_button(
        label="Download Notebook",
        data=file,
        file_name="project_romanbokhyan.ipynb",
        mime="application/x-ipynb+json"
    )
st.write("[Dataset](https://www.kaggle.com/datasets/whenamancodes/alcohol-effects-on-study)")
st.write('[GitHub](https://github.com/7AMP77/alcohol_analyze_dsba222)')