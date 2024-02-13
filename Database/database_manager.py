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
                        first_name VARCHAR(255),
                        last_name VARCHAR(255),
                        password TEXT,
                        salt TEXT
                    )
                ''')
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS quotes (
                        quote_id SERIAL PRIMARY KEY,
                        company_name VARCHAR(255),
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')

        self.connection.commit()

    def get_password(self, username):
        try:
            self.cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
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
            self.cursor.execute("SELECT salt FROM users WHERE username = %s", (username,))
            result = self.cursor.fetchone()

            if result:
                return result
            else:
                return None
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def create(self, username, first_name, last_name, hashed_pass, salt):  # creating a user
        try:
            self.cursor.execute("SELECT username FROM users WHERE username = %s", (username,))
            existing_username = self.cursor.fetchone()

            if existing_username:
                return False

            db_pass = hashed_pass.decode('utf-8')
            self.cursor.execute(
                "INSERT INTO users (username, first_name, last_name, password, salt) VALUES (%s, %s, %s, %s, %s)",
                (username, first_name, last_name, db_pass, salt))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    # Get the first and last name of the current user
    def get_curr_user(self, username):
        pass
        try:
            self.cursor.execute("SELECT first_name, last_name FROM users WHERE username = %s", (username,))
            result = self.cursor.fetchall()

            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f"Usernames Error: {e}")
            return False
