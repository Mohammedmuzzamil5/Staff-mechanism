import sqlite3

class StaffDB:
    def __init__(self):
        self.conn = sqlite3.connect('staff_information.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                qualifications TEXT,
                role TEXT,
                contact_number TEXT
            )
        ''')
        self.conn.commit()

    def add_staff(self, name, age, qualifications, role, contact_number):
        self.cursor.execute('''
            INSERT INTO staff (name, age, qualifications, role, contact_number)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, age, qualifications, role, contact_number))
        self.conn.commit()

    def get_all_staff(self):
        self.cursor.execute('SELECT * FROM staff')
        return self.cursor.fetchall()

    def update_staff(self, staff_id, name, age, qualifications, role, contact_number):
        self.cursor.execute('''
            UPDATE staff
            SET name=?, age=?, qualifications=?, role=?, contact_number=?
            WHERE id=?
        ''', (name, age, qualifications, role, contact_number, staff_id))
        self.conn.commit()

    def delete_staff(self, staff_id):
        self.cursor.execute('DELETE FROM staff WHERE id=?', (staff_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()
