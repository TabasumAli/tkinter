# database.py
import sqlite3







class Database:
    def __init__(self, db_file='your_database_file.db'):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Define your database schema here
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                name TEXT,
                department TEXT,
                salary REAL
            )
        """)
        # Define other tables (clients, events, guests, venues) similarly...

    def get_employees(self):
        self.cur.execute("SELECT * FROM employees")
        return self.cur.fetchall()

    def update_employee(self, id, name, department, salary):
        self.cur.execute("UPDATE employees SET name=?, department=?, salary=? WHERE id=?", (name, department, salary, id))
        self.conn.commit()

    def delete_employee(self, id):
        self.cur.execute("DELETE FROM employees WHERE id=?", (id,))
        self.conn.commit()
