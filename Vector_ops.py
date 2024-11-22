import sqlite3
import json

def add_vector_to_db(conn, id, vector):
    cursor = conn.cursor()
    vector_str = json.dumps(vector)
    cursor.execute("INSERT OR REPLACE INTO vectors (id, vector) VALUES (?, ?)", (id, vector_str))
    conn.commit()

def get_vector_from_db(conn, id):
    cursor = conn.cursor()
    cursor.execute("SELECT vector FROM vectors WHERE id = ?", (id,))
    result = cursor.fetchone()
    if result:
        return json.loads(result[0])
    return None
