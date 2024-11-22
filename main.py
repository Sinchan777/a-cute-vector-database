import sqlite3
from vector_operations import add_vector_to_db, get_vector_from_db
import numpy as np

def generate_random_vector(dim=128):
    return np.random.rand(dim).tolist()

def main():
    conn = sqlite3.connect("vectors.db")
    add_vector_to_db(conn, 1, generate_random_vector())
    add_vector_to_db(conn, 2, generate_random_vector())

    vector = get_vector_from_db(conn, 1)
    print(f"Retrieved vector for ID 1: {vector}")

if __name__ == "__main__":
    main()
