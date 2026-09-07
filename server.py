from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = "ai_resq.db"


# =========================================
# DATABASE INITIALIZATION
# =========================================

def init_db():

    conn = sqlite3.connect(DATABASE)

    # Create table if it does not exist
    conn.execute("""
        CREATE TABLE IF NOT EXISTS missions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            survivor TEXT,
            condition TEXT,
            priority TEXT,
            distance TEXT,
            status TEXT
        )
    """)

    # Check existing columns
    columns = conn.execute(
        "PRAGMA table_info(missions)"
    ).fetchall()

    column_names = [column[1] for column in columns]

    # Add status column to old database
    if "status" not in column_names:
        conn.execute(
            "ALTER TABLE missions ADD COLUMN status TEXT"
        )

    conn.commit()
    conn.close()


# =========================================
# HOME
# =========================================

@app.route("/")
def home():

    return "AI-ResQ Backend is Running!"


# =========================================
# BACKEND STATUS
# =========================================

@app.route("/api/status")
def status():

    return jsonify({
        "project": "AI-ResQ",
        "status": "Active",
        "message": "Backend connected successfully"
    })


# =========================================
# SAVE MISSION
# =========================================

@app.route("/api/save-mission", methods=["POST"])
def save_mission():

    try:

        data = request.get_json()

        conn = sqlite3.connect(DATABASE)

        conn.execute("""
            INSERT INTO missions
            (survivor, condition, priority, distance, status)
            VALUES (?, ?, ?, ?, ?)
        """, (
            data["survivor"],
            data["condition"],
            data["priority"],
            data["distance"],
            data["status"]
        ))

        conn.commit()
        conn.close()

        return jsonify({
            "message": "Mission saved successfully"
        })

    except Exception as error:

        return jsonify({
            "message": "Failed to save mission",
            "error": str(error)
        }), 500


# =========================================
# VIEW MISSION RECORDS
# =========================================

@app.route("/api/missions")
def get_missions():

    try:

        conn = sqlite3.connect(DATABASE)

        cursor = conn.execute("""
            SELECT
                id,
                survivor,
                condition,
                priority,
                distance,
                status
            FROM missions
        """)

        missions = cursor.fetchall()

        conn.close()

        records = []

        for mission in missions:

            records.append({
                "id": mission[0],
                "survivor": mission[1],
                "condition": mission[2],
                "priority": mission[3],
                "distance": mission[4],
                "status": mission[5]
            })

        return jsonify(records)

    except Exception as error:

        return jsonify({
            "message": "Failed to load records",
            "error": str(error)
        }), 500


# =========================================
# START SERVER
# =========================================

if __name__ == "__main__":

    init_db()

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )