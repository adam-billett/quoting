from Database import database_manager
import psycopg2


class QuoteDatabase:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    # Method to get the quote id
    def get_quote_id(self):
        try:
            query = "SELECT quote_id FROM quotes ORDER BY date DESC LIMIT 1"
            cursor = self.db_manager.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)

            if result:
                return result[0]
            else:
                return None

        except Exception as e:
            print(f"Get quote id fail: {e}")

    # method to add the quote
    def add_quote_id(self, quote_id, company_name):
        try:
            query = "INSERT INTO quotes (quote_id, company_name) VALUES (%s, %s)"
            self.db_manager.cursor.execute(query, (quote_id, company_name))
            self.db_manager.connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False

    def get_company_name(self):
        try:
            query = "SELECT company_name FROM quotes"
            result = self.db_manager.connection.execute(query).fetchone()

            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print(f'Error: {e}')

    def get_quotes(self):
        try:
            query = "SELECT company, date FROM quotes"
            self.db_manager.connection.execute(query)
            quotes = self.db_manager.fetchall()
            return quotes
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
