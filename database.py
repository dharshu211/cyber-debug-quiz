import sqlite3
import json
from pathlib import Path

DATABASE = Path(__file__).with_name("cyberdb.sqlite3")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            team_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            email TEXT NOT NULL,
            team_name TEXT NOT NULL,
            set_number INTEGER NOT NULL,
            score INTEGER NOT NULL,
            max_score INTEGER NOT NULL,
            time_taken INTEGER NOT NULL,
            status TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            answers_json TEXT DEFAULT '{}'
        )
    """)

    # Backward-compatible migration for databases created by older versions.
    columns = {row[1] for row in cursor.execute("PRAGMA table_info(results)").fetchall()}
    if "answers_json" not in columns:
        cursor.execute("ALTER TABLE results ADD COLUMN answers_json TEXT DEFAULT '{}'" )

    connection.commit()
    connection.close()


def save_student(name, email, team_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO students (name, email, team_name) VALUES (?, ?, ?)",
        (name, email, team_name),
    )
    student_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return student_id


def save_result(name, email, team_name, set_number, score, max_score, time_taken, status, answers=None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO results
        (student_name, email, team_name, set_number, score, max_score, time_taken, status, answers_json)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (name, email, team_name, set_number, score, max_score, time_taken, status, json.dumps(answers or {}, ensure_ascii=False)))
    result_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return result_id


def get_leaderboard():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id, student_name, email, team_name, set_number, score, max_score,
               time_taken, status, submitted_at, answers_json
        FROM results
        ORDER BY score DESC,
                 CASE WHEN status = 'Completed' THEN 0 ELSE 1 END,
                 time_taken ASC,
                 submitted_at ASC
    """)
    rows = cursor.fetchall()
    connection.close()
    return rows



def get_result(result_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM results WHERE id = ?", (result_id,))
    row = cursor.fetchone()
    connection.close()
    return row


def delete_result(result_id):
    """Delete one result row by its database id."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM results WHERE id = ?", (result_id,))
    deleted = cursor.rowcount > 0
    connection.commit()
    connection.close()
    return deleted


def clear_results():
    """Delete every result from the official leaderboard."""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM results")
    deleted_count = cursor.rowcount
    connection.commit()
    connection.close()
    return deleted_count
