import psycopg2


class DatabaseManager:

    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id SERIAL PRIMARY KEY,
                        username VARCHAR(255),
                        password TEXT,
                        salt TEXT,
                    )
                ''')
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS quotes (
                        quote_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(255),
                        company_address VARCHAR(255),
                        date TIME STAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

    def get_password(self, username):
        try:
            self.cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchone()

            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Error occurred: {e}")

    # Get salt from the db
    def get_salt(self, username):
        try:
            self.cursor.execute("SELECT salt FROM users WHERE username = ?", (username,))
            result = self.cursor.fetchone()

            if result:
                return result
            else:
                return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
