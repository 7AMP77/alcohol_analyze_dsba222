import streamlit as st
import plotly.express as px


def drawpie(df, values):
    fig = px.pie(df, values=values, names=values)
    st.plotly_chart(fig)


def drawbox(df, x, y):
    fig = px.box(df, x=x, y=y)
    st.plotly_chart(fig)


def drawbar(df, x, y):
    fig = px.bar(df, x=x, y=y)
    st.plotly_chart(fig)


def drawline(df, x, y):
    fig = px.line(df, x=x, y=y)
    st.plotly_chart(fig)


def drawscatter(df, x, y):
    fig = px.scatter(df, x=x, y=y)
    st.plotly_chart(fig)
