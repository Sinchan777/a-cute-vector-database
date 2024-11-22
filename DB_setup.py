import sqlite3

def setup_database():
    conn = sqlite3.connect("vectors.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vectors (
        id INTEGER PRIMARY KEY,
        vector TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
