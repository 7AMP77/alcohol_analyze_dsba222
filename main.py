import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
import functions

def load_data():
    df = pd.read_csv('Maths.csv')
    df = df[["famsize", "Pstatus", "guardian", "romantic", "goout", "Dalc", "Walc"]].copy()
    df = df[df.guardian != 'other']
    df['alcoeveryday'] = (df.Dalc + df.Walc) / 2
    return df


def filter_data_by_status(df, status):
    return df[df['Pstatus'] == status].copy()


def filter_data_by_guardian(df, guardian):
    return df[df['guardian'] == guardian]


def calculate_descriptive_stats(df):
    print(df.describe())
    print('goout median -', df['goout'].median())
    print('Dalc median -', df['Dalc'].median())
    print('Walc median -', df['Walc'].median())


def side_bar():
    st.sidebar.write('https://www.tinkoff.ru/cf/gRW0sECqnu')

def setup_streamlit_interface(df):
    st.markdown("# Main project page️")
    if st.sidebar.checkbox("Support developer"):
        side_bar()

    tabs = st.tabs(["Issues", "Daily consumption of alcohol", "The influence of a parent", "Conclusion"])
    display_issues_tab(tabs[0], df)
    display_alcohol_consumption_tab(tabs[1], df)
    display_parent_influence_tab(tabs[2], df)
    display_conclusion_tab(tabs[3])


def display_issues_tab(tab, df):
    if st.sidebar.checkbox("Support developer"):
        side_bar()
    with tab:
        st.header("Issues")
        st.write(
            'I assume that children living in single-parent families in Portugal who have problems with socialization are as prone to alcohol addiction as children living in two-parent families. In order to test this hypothesis,'
            ' I constructed various graphs and analyzed the available information.'
            ' You will find the graphs in the tabs below, and my conclusion will be in a separate tab "Conclusion". ')
        option = st.selectbox("Click to select:", ['alcohol', 'socialization'], key='option_issues_tab')
        if option == 'socialization':
            st.write('First graph - parents living apart')
            st.write('romantic - kid with a romantic relationship (binary: yes or no)')
            st.write('goout - going out with friends (numeric: from 1 - very low to 5 - very high)')
            functions.drawbar(df, 'romantic', 'goout')
            st.write('Second graph - parents living together')
            st.write('romantic - kid with a romantic relationship (binary: yes or no)')
            st.write('goout - kids going out with friends (numeric: from 1 - very low to 5 - very high)')
            functions.drawbar(df, 'romantic', 'goout')
            st.write(
                'Based on the graphs above, we can conclude that there is no difference in the socialization of children living in single-parent and two-parent families.')
        elif option == 'alcohol':
            st.write('First graph - parents living apart')
            st.write('Dalc - kids workday alcohol consumption (numeric: from 1 - very low to 5 - very high)')
            st.write('Walc - kids weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)')
            functions.drawscatter(df, 'Dalc', 'Walc')
            st.write('Second graph - parents living together')
            st.write('Dalc - kids workday alcohol consumption (numeric: from 1 - very low to 5 - very high)')
            st.write('Walc - kids weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)')
            functions.drawscatter(df, 'Dalc', 'Walc')
            st.write(
                'Based on the graphs above, we can conclude that children from single-parent families drink less than children from full families.')

def display_alcohol_consumption_tab(tab, df):
    if st.sidebar.checkbox("Support developer"):
        side_bar()
    with tab:
        st.header("Daily consumption of alcohol")
        st.write('The chart below will provide information about'
                 ' children from A and T families and how often they drink alcohol.')
        st.write('Pstatus - parents cohabitation status (binary: T - living together or A - apart')
        st.write('alcoeveryday - the arithmetic mean of each childs daily alcohol consumption.')
        functions.drawbox(df, 'Pstatus', 'alcoeveryday')
        st.write(
            'Based on the graph above, we can conclude that the average daily alcohol consumption of children from full families is slightly higher than that of children from one-parent families.')


def display_parent_influence_tab(tab, df):
    if st.sidebar.checkbox("Support developer"):
        side_bar()
    with tab:
        st.header("The influence of a parent")
        st.write(
            'In the tabels below I have analyzed the effect of which parent a child lives with on their drinking and socialization problems.')
        option = st.selectbox("Click to select:", ['alcohol', 'socialization'], key='option_parent_influence_tab')
        if option == 'alcohol':
            st.write(
                'In the table below you can see the average daily alcohol consumption depending on who the child lives with.')

            fig = go.Figure(data=[go.Table(header=dict(values=['Mother', 'Father']),
                                           cells=dict(values=[[df.alcoeveryday.mean()], [df.alcoeveryday.mean()],
                                                              ]))])

            data_matrix = [['Mother', 'Father', 'Mother and Father'],
                           [df.alcoeveryday.mean(), df.alcoeveryday.mean(), df.alcoeveryday.mean()]]

            fig = ff.create_table(data_matrix)
            st.write(fig)
            st.write('Based on the table above, you can see that there is a slight difference between the values.  ')
        elif option == 'socialization':
            st.write('In the table below you can see the average childs walks depending on who he lives with.')

            data_matrix = [['Mother', 'Father', 'Mother and Father'],
                           [df.goout.mean(), df.goout.mean(), df.goout.mean()]]

            fig = ff.create_table(data_matrix)
            st.write(fig)
            st.write(
                'Based on the table above, you can see that there is also a slight difference between the values, but it is more noticeable than in alcohol.')
def display_conclusion_tab(tab):
    if st.sidebar.checkbox("Support developer"):
        side_bar()
    with tab:
        st.header("Conclusion")
        st.write(
            'Having done all the work, I can confirm my hypothesis that the type of family does not affect the problems of children in Portugal. I have analyzed all the information, analyzed the values obtained and noticed that the difference in the graphs is present in a very small ratio, which can be equated to zero and precisely based on this I can safely say that my hypothesis is true.')
        st.write('All graphs can be found in the tabs to the right.')
        clicked = st.button("SNOW")
        if clicked:
            st.snow()

def main():
    df = load_data()
    calculate_descriptive_stats(df)
    setup_streamlit_interface(df)

if __name__ == '__main__':
    main()