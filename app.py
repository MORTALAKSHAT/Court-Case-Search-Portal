from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Simulate dummy response from court portal
def get_dummy_case_info(case_type, case_no, filing_year):
    return {
        "Parties": "John Doe vs State of XYZ",
        "Filing Date": "2023-01-15",
        "Next Hearing": "2025-08-20",
        "PDF Link": "https://example.com/dummy-judgment.pdf"
    }

# SQLite setup (1-time creation, or run separately)
def init_db():
    conn = sqlite3.connect("queries.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_no TEXT,
            filing_year TEXT,
            timestamp TEXT,
            raw_response TEXT
        )
    """)
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("form.html")  # your HTML file

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    case_type = data.get("case_type")
    case_no = data.get("case_no")
    filing_year = data.get("filing_year")

    result = get_dummy_case_info(case_type, case_no, filing_year)

    # Log query and dummy response
    conn = sqlite3.connect("queries.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO logs (case_type, case_no, filing_year, timestamp, raw_response) VALUES (?, ?, ?, ?, ?)",
                (case_type, case_no, filing_year, datetime.now().isoformat(), str(result)))
    conn.commit()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)






import sqlite3

conn = sqlite3.connect("queries.db")
cur = conn.cursor()
cur.execute("SELECT * FROM logs")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
