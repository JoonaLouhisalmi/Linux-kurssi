from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    # Yhdistetään MariaDB/MySQL-tietokantaan
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="MyAppDbPass2025",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    # Palautetaan HTML-sivu
    return f"""
    <html>
    <head><title>LEMP Example App</title></head>
    <body style="font-family:sans-serif; text-align:center; margin-top:50px;">
        <h1>LEMP Stack toimii 🎉</h1>
        <p>Hello from MySQL!</p>
        <p><b>Server time:</b> {result[0]}</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
