import streamlit as st
import pandas as pd
import mysql.connector
import altair as alt

st.title("Data Analysis Dashboard")
st.write("Sää- ja Bitcoin-data päivittyy automaattisesti 15 minuutin välein cron-tehtävien avulla.")

# --- MySQL-yhteys ---
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="stream",
        password="streampass",
        database="testidb"
    )

# --- WEATHER DATA ---
st.header("🌤️ Säädata (Helsinki)")

conn = get_connection()
df_weather = pd.read_sql("SELECT * FROM weather_data ORDER BY timestamp DESC", conn)
conn.close()

st.subheader("Viimeisin data")
st.write(df_weather.head(1))

st.subheader("Säädata taulukkona")
st.dataframe(df_weather)

chart_weather = alt.Chart(df_weather).mark_line(point=True).encode(
    x='timestamp:T',
    y='temperature:Q',
    tooltip=['timestamp', 'temperature', 'description']
).properties(title="Lämpötila ajan mukaan")

st.altair_chart(chart_weather, use_container_width=True)


# --- BITCOIN DATA ---
st.header("₿ Bitcoin (BTC/EUR)")

conn = get_connection()
df_crypto = pd.read_sql("SELECT * FROM crypto_data ORDER BY timestamp DESC", conn)
conn.close()

st.subheader("Viimeisin BTC-arvo")
st.write(df_crypto.head(1))

st.subheader("Bitcoin-hinta taulukkona")
st.dataframe(df_crypto)

chart_crypto = alt.Chart(df_crypto).mark_line(point=True).encode(
    x='timestamp:T',
    y='price:Q',
    tooltip=['timestamp', 'price']
).properties(title="Bitcoin-hinta ajan mukaan (EUR)")

st.altair_chart(chart_crypto, use_container_width=True)
