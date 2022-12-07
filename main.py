'Hypotheze - Kids living in single-parent families in Portugal who also have socialization problems tend to have problems with alcochol consumption.'
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import functions

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
print('Lets check columns on NaN elements:')
for i in range(len(list_of_columns)):
    print('column ', list_of_columns[i], '-', df2[list_of_columns[i]].isnull().values.any())
print('It can be clearly seen that there are no such columns with NaN elements, so there are nothing to remove.')
print()
print('The DataFrame object after deliting unnecessary columns and checking rows on NaN.')
print(df2)
print()
print('Lets find descriptive statistics')
print(df2.describe())
print('goout median -', df2['goout'].median())
print('Dalc median -', df2['Dalc'].median())
print('Walc median -', df2['Walc'].median())

plt.style.use('_mpl-gallery')
df2.sort_values(by=['goout', 'Dalc'])

if st.sidebar.checkbox("Поддержать разработчика"):
    st.sidebar.write('https://www.tinkoff.ru/cf/1bssNH3paO6')
print('Lets look at the statistics of children living in single-parent and two-parent families.')
df3 = df2[df2['Pstatus'] == 'A'].copy()
df4 = df2[df2['Pstatus'] == 'T'].copy()
print('As a reminder, all the explanations of all the symbols that appear in the table can be found above.')
print('How many kids living in A families have problems with socialization')
levels_sat = sorted(list(df["romantic"].unique()))
mass = []
mass2 = []
option = st.selectbox("Issues", (['socialization', 'alcochol']))
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

print('How many kids living in T families have problems with socialization')


print(df4.info())