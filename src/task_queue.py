import sqlite3
from datetime import datetime

class TaskQueue:
    def __init__(self, db_path='tasks.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                priority INTEGER DEFAULT 1,
                status TEXT DEFAULT 'pending',
                created_at TEXT
            )
        ''')

        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                goal_id INTEGER,
                description TEXT,
                agent_role TEXT DEFAULT 'coder',
                status TEXT DEFAULT 'pending',
                output TEXT,
                created_at TEXT,
                FOREIGN KEY(goal_id) REFERENCES goals(id)
            )
        ''')
        self.conn.commit()
