import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px


st.title("Streamlit toimii!")
st.write("Virtuaaliympäristö ja paketit ovat kunnossa.")
st.write("Alla näkyy MySQL-tietokannan data:")

# MySQL-yhteys
conn = mysql.connector.connect(
    host="localhost",
    user="stream",
    password="streampass",
    database="testidb"
)

# Lue data DataFrameen
df = pd.read_sql("SELECT * FROM mittaukset", conn)

# Näytä taulukko
st.dataframe(df)

# Pylväsdiagrammi mittausten arvoista
fig = px.bar(
    df,
    x="nimi",
    y="arvo",
    title="Mittaukset pylväsdiagrammina",
    labels={"nimi": "Mittaus", "arvo": "Arvo"}
)

st.plotly_chart(fig)

conn.close()
