from flask import Flask, jsonify, request
import mysql.connector
import os

app = Flask(__name__)

# Ympäristömuuttujat (k8s ConfigMap ja Secret)
DB_HOST = os.getenv("DB_HOST", "mysql")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "changeme")
DB_NAME = os.getenv("DB_NAME", "appdb")


def get_conn():
    """Luo tietokantayhteys"""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


# -----------------------------
#       API ENDPOINTIT
# -----------------------------

@app.get("/api/health")
def health():
    """Terveystarkistus"""
    return {"status": "ok"}


@app.get("/api")
def index():
    """Yksinkertainen testi MySQL-yhteyteen"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from MySQL via Flask!'")
    row = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(message=row[0])


@app.get("/api/users")
def get_users():
    """Hae kaikki käyttäjät"""
    try:
        conn = get_conn()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.post("/api/add")
def add_user():
    """Lisää uusi käyttäjä tietokantaan"""
    try:
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        if not name or not email:
            return jsonify({"error": "name and email required"}), 400

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email),
        )
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "user added successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
#   Kehityskäyttöä varten
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
