import pandas as pd
import streamlit as st
import plotly.express as px

st.title("Site")

nome = st.text_input("Digite seu nome")

if nome:
    st.write(f"Olá, {nome}!")