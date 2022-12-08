'Hypotheze - Kids living in single-parent families in Portugal who also have socialization problems tend to have problems with alcochol consumption.'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import functions

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

plt.style.use('_mpl-gallery')
df2.sort_values(by=['goout', 'Dalc'])
print('lets add a new column that will show alcohol consumption per week ')

df_new = df2.assign(alcoeveryday=lambda x: (x.Dalc + x.Walc) / 2)
print(df_new)

if st.sidebar.checkbox("Поддержать разработчика"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')

print('Lets look at the statistics of children living in single-parent and two-parent families.')

df3 = df_new[df_new['Pstatus'] == 'A'].copy()
df4 = df_new[df_new['Pstatus'] == 'T'].copy()
print('As a reminder, all the explanations of all the symbols that appear in the table can be found above.')

print('How many kids living in A families have problems with socialization')
print('How many kids living in T families have problems with socialization')
levels_sat = sorted(list(df["romantic"].unique()))
mass = []
mass2 = []

tab1, tab2, tab3 = st.tabs(["Issues", "Daily consumption of alcohol", "Conclusion"])
with tab1:
    st.header("Issues")
    st.write('I assume that children living in single-parent families in Portugal who have problems with socialization are prone to alcohol addiction. In order to test this hypothesis,'
             ' I constructed various graphs and analyzed the available information.'
             ' You will find the graphs in the tabs below, and my conclusion will be in a separate tab "Conclusion". ')
    option = st.selectbox("", (['socialization', 'alcochol']))

    if option == 'socialization':
        for el in levels_sat:
            mass.append((df3[df3["romantic"] == el])["goout"].mean())
        functions.drawbar(levels_sat, mass, "romantic", "goout")
        for el in levels_sat:
            mass2.append((df4[df4["romantic"] == el])["goout"].mean())
        functions.drawbar(levels_sat, mass2, "romantic", "goout")
    if option == 'alcochol':
        levels_sat = ['Dalc', 'Walc']
        for el in levels_sat:
            mass.append(df3[el].mean())
        functions.drawline(levels_sat, mass, "day", "alc ")
        for el in levels_sat:
            mass2.append(df4[el].mean())
        functions.drawline(levels_sat, mass2, "day", "alc")
with tab2:
    st.header("Daily consumption of alcohol")


with tab3:
    st.header("Conclusion")