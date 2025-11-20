# Viikkotehtävä 4 – Cron + API + MySQL + Streamlit

Tässä tehtävässä toteutin kaksi automaattista datankeruuta cronin avulla:
- OpenWeatherMap API hakee säädatan 15 minuutin välein
- Binance API hakee Bitcoin-hinnan 15 minuutin välein

Datan tallennus tapahtuu MySQL/MariaDB-tietokantaan kahteen tauluun:
- weather_data
- crypto_data

Streamlit-sovellus näyttää reaaliaikaisesti tietokannan sisällön (päivittyy automaattisesti).
