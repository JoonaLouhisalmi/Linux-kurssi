#!/usr/bin/env python3
import requests
import mysql.connector
from datetime import datetime

# CoinGecko API
URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur"

# MySQL-yhteys (samat kuin säädatassa)
conn = mysql.connector.connect(
    host='localhost',
    user='stream',
    password='streampass',
    database='testidb'
)

cursor = conn.cursor()

# Luo BTC-taulu jos puuttuu
cursor.execute("""
CREATE TABLE IF NOT EXISTS crypto_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(20),
    price FLOAT,
    timestamp DATETIME
)
""")

# Hae hinta
resp = requests.get(URL).json()
price = resp["bitcoin"]["eur"]
timestamp = datetime.now()

# Tallenna tietokantaan
cursor.execute(
    "INSERT INTO crypto_data (symbol, price, timestamp) VALUES (%s, %s, %s)",
    ("BTC", price, timestamp)
)

conn.commit()
cursor.close()
conn.close()

print(f"BTC price saved: {price} EUR")
