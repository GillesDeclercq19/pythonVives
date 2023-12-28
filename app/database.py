import sqlite3

class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)
        self.connection.commit()

    def fetch_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
    
        columns = [col[0] for col in self.cursor.description]
        result = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return result


    def __del__(self):
        self.connection.close()
