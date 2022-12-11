'Hypothesis - Children living in full families in Portugal and in single-parent families have the same problems with socialization and tendency to alcohol dependence.'
import numpy as np
import pandas as pd
import streamlit as st
import functions
import plotly.graph_objects as go
import plotly.figure_factory as ff

st.markdown("# Main project page️")

df = pd.read_csv('Maths.csv')

df2 = df[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
df2 = df2[df2.guardian != 'other']
df_new = df2.assign(alcoeveryday=lambda x: (x.Dalc + x.Walc) / 2)
df3 = df_new[df_new['Pstatus'] == 'A'].copy()
df4 = df_new[df_new['Pstatus'] == 'T'].copy()
df5 = df_new[df_new['guardian'] == 'mother']
df6 = df_new[df_new['guardian'] == 'father']
list_of_columns = ["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]
print(df2)
print()
print('Lets find descriptive statistics')
print(df2.describe())
print('goout median -', df2['goout'].median())
print('Dalc median -', df2['Dalc'].median())
print('Walc median -', df2['Walc'].median())

df2.sort_values(by=['goout', 'Dalc'])
print('lets add a new column that will show alcohol consumption per week ')

print(df_new)

if st.sidebar.checkbox("Support developer"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')

print('Lets look at the statistics of children living in single-parent and two-parent families.')

levels_sat = sorted(list(df["romantic"].unique()))
mass = []
mass2 = []

tab1, tab2, tab3, tab4 = st.tabs(["Issues", "Daily consumption of alcohol", "The influence of a parent", "Conclusion"])
with tab1:
    st.header("Issues")
    st.write(
        'I assume that children living in single-parent families in Portugal who have problems with socialization are as prone to alcohol addiction as children living in two-parent families. In order to test this hypothesis,'
        ' I constructed various graphs and analyzed the available information.'
        ' You will find the graphs in the tabs below, and my conclusion will be in a separate tab "Conclusion". ')

    option = st.selectbox("click to select", (['socialization', 'alcohol']))

    if option == 'socialization':
        st.write('First graph - parents living apart')
        st.write('romantic - kid with a romantic relationship (binary: yes or no)')
        st.write('goout - going out with friends (numeric: from 1 - very low to 5 - very high)')
        functions.drawbar(df3, 'romantic', 'goout')
        st.write('Second graph - parents living together')
        st.write('romantic - kid with a romantic relationship (binary: yes or no)')
        st.write('goout - kids going out with friends (numeric: from 1 - very low to 5 - very high)')
        functions.drawbar(df4, 'romantic', 'goout')
        st.write(
            'Based on the graphs above, we can conclude that there is no difference in the socialization of children living in single-parent and two-parent families.')

    if option == 'alcohol':
        st.write('First graph - parents living apart')
        st.write('Dalc - kids workday alcohol consumption (numeric: from 1 - very low to 5 - very high)')
        st.write('Walc - kids weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)')
        functions.drawscatter(df3, 'Dalc', 'Walc')
        st.write('Second graph - parents living together')
        st.write('Dalc - kids workday alcohol consumption (numeric: from 1 - very low to 5 - very high)')
        st.write('Walc - kids weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)')
        functions.drawscatter(df4, 'Dalc', 'Walc')
        st.write(
            'Based on the graphs above, we can conclude that children from single-parent families drink less than children from full families.')

with tab2:
    st.header("Daily consumption of alcohol")
    st.write('The chart below will provide information about'
             ' children from A and T families and how often they drink alcohol.')
    st.write('Pstatus - parents cohabitation status (binary: T - living together or A - apart')
    st.write('alcoeveryday - the arithmetic mean of each childs daily alcohol consumption.')
    functions.drawbox(df_new, 'Pstatus', 'alcoeveryday')
    st.write(
        'Based on the graph above, we can conclude that the average daily alcohol consumption of children from full families is slightly higher than that of children from one-parent families.')
with tab3:
    st.header("The influence of a parent")
    st.write(
        'In the tabels below I have analyzed the effect of which parent a child lives with on their drinking and socialization problems.')
    option = st.selectbox("click to select ", (['alcohol', 'socialization']))
    if option == 'alcohol':
        st.write(
            'In the table below you can see the average daily alcohol consumption depending on who the child lives with.')

        fig = go.Figure(data=[go.Table(header=dict(values=['Mother', 'Father']),
                                       cells=dict(values=[[df5.alcoeveryday.mean()], [df6.alcoeveryday.mean()],
                                                          ]))])

        data_matrix = [['Mother', 'Father', 'Mother and Father'],
                       [df5.alcoeveryday.mean(), df6.alcoeveryday.mean(), df_new.alcoeveryday.mean()]]

        fig = ff.create_table(data_matrix)
        st.write(fig)
        st.write('Based on the table above, you can see that there is a slight difference between the values.  ')
    if option == 'socialization':
        st.write('In the table below you can see the average childs walks depending on who he lives with.')

        data_matrix = [['Mother', 'Father', 'Mother and Father'],
                       [df5.goout.mean(), df6.goout.mean(), df_new.goout.mean()]]

        fig = ff.create_table(data_matrix)
        st.write(fig)
        st.write(
            'Based on the table above, you can see that there is also a slight difference between the values, but it is more noticeable than in alcohol.')
with tab4:
    st.header("Conclusion")
    st.write(
        'Having done all the work, I can confirm my hypothesis that the type of family does not affect the problems of children in Portugal. I have analyzed all the information, analyzed the values obtained and noticed that the difference in the graphs is present in a very small ratio, which can be equated to zero and precisely based on this I can safely say that my hypothesis is true.')
    st.write('All graphs can be found in the tabs to the right.')
    clicked = st.button("SNOW")
    if clicked:
        st.snow()

