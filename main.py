'Hypothesis - Children living in full families in Portugal and in single-parent families have the same problems with socialization and tendency to alcohol dependence.'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import functions
import plotly.express as px

st.markdown("# Main project page️")

df = pd.read_csv('Maths.csv')

print('We need only "famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc" and "Walc" columns.')
print()
print('Columns meanings are:'
      ' famize - family size, LE3 - less or equal to 3 or GT3 - greater than 3;', '\n'
                                                                                  'Pstatus - parents cohabitation status, T - living together or A - apart;',
      '\n'
      'guardian - students guardian ,nominal: mother, father or other;', '\n'
                                                                         'romantic - with a romantic relationship, binary: yes or no;',
      '\n'
      'goout - going out with friends, numeric: from 1 - very low to 5 - very high;', '\n'
                                                                                      'Dalc - workday alcohol consumption,numeric: from 1 - very low to 5 - very high;',
      '\n'
      'Walc - weekend alcohol consumption, numeric: from 1 - very low to 5 - very high;')
print()
print('The DataFrame object before deliting unnecessary columns and checking rows on NaN.')

print(df)

df2 = df[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
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

df_new = df2.assign(alcoeveryday=lambda x: (x.Dalc + x.Walc) / 2)
print(df_new)

if st.sidebar.checkbox("Support developer"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')

print('Lets look at the statistics of children living in single-parent and two-parent families.')

df3 = df_new[df_new['Pstatus'] == 'A'].copy()
df4 = df_new[df_new['Pstatus'] == 'T'].copy()
df5 = df_new[df_new['guardian'] == 'mother']
df6 = df_new[df_new['guardian'] == 'father']
print('As a reminder, all the explanations of all the symbols that appear in the table can be found above.')

levels_sat = sorted(list(df["romantic"].unique()))
mass = []
mass2 = []
tmp3 = df3
tmp4 = df4

tab1, tab2, tab3, tab4 = st.tabs(["Issues", "Daily consumption of alcohol", "The influence of a parent", "Conclusion"])
with tab1:
    st.header("Issues")
    st.write(
        'I assume that children living in single-parent families in Portugal who have problems with socialization are as prone to alcohol addiction as children living in two-parent families. In order to test this hypothesis,'
        ' I constructed various graphs and analyzed the available information.'
        ' You will find the graphs in the tabs below, and my conclusion will be in a separate tab "Conclusion". ')
    st.write('First graph - parents living apart')
    st.write('Second graph - parents living together')
    option = st.selectbox("click to select", (['socialization', 'alcohol']))

    if option == 'socialization':
        functions.drawbar(tmp3, 'romantic', 'goout')
        functions.drawbar(tmp4, 'romantic', 'goout')

    if option == 'alcohol':
        functions.drawscatter(tmp3, 'Dalc', 'Walc')
        functions.drawscatter(tmp4, 'Dalc', 'Walc')

with tab2:
    st.header("Daily consumption of alcohol")
    st.write('The chart below will provide information about'
             ' children from A and T families and how often they use alcohol.')
    st.write('P.S. A - parents living apart, T - parents living together')
    functions.drawbox(df_new, 'Pstatus', 'alcoeveryday')
with tab3:
    st.header("The influence of a parent")
    st.write(
        'In the tabels below I have analyzed the effect of which parent a child lives with on their drinking and socialization problems.')
    option = st.selectbox("click to select ", (['alcohol', 'socialization']))
    if option == 'alcohol':
        st.write(
            'In the table below you can see the average daily alcohol consumption depending on who the child lives with.')
        import plotly.graph_objects as go

        fig = go.Figure(data=[go.Table(header=dict(values=['Mother', 'Father', 'Mother and Father']),
                                       cells=dict(values=[[df5.alcoeveryday.mean()], [df6.alcoeveryday.mean()],
                                                          [df_new.alcoeveryday.mean()]]))])
        st.write(fig)
    if option == 'socialization':
        st.write('In the table below you can see the average childs walks depending on who he lives with.')
        import plotly.figure_factory as ff

        data_matrix = [['Mother', 'Father', 'Mother and Father'],
                       [df5.goout.mean(), df6.goout.mean(), df_new.goout.mean()]]

        fig = ff.create_table(data_matrix)
        st.write(fig)

with tab4:
    st.header("Conclusion")
    st.write(
        'Having done all the work, I can confirm my hypothesis that the type of family does not affect the problems of children in Portugal. I have analyzed all the information, analyzed the values obtained and noticed that the difference in the graphs is present in a very small ratio, which can be equated to zero and precisely based on this I can safely say that my hypothesis is true.')
    st.write('All graphs can be found in the tabs to the right.')
    clicked = st.button("BALOONS")
    if clicked:
        st.balloons()
print(df_new)
print(df['romantic'].value_counts())
df_check = pd.DataFrame({'P'})
print(df5)
