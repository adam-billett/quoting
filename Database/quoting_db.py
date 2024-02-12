from Database import database_manager
import psycopg2


class QuoteDatabase:
    def __int__(self, db_manager):
        self.db_manager = db_manager

    # Method to get the quote id
    def get_quote_id(self):
        try:
            query = "SELECT quote_id FROM quotes WHERE company_name = %s"
            self.db_manager.connection.execute(query)
            result = self.db_manager.cursor.fetchone()

            if result:
                return True
            else:
                return None

        except Exception as e:
            print(f"Error: {e}")

    # method to add the quote
    def add_quote_id(self, quote_id):
        try:
            query = "INSERT INTO quotes (quote_id) VALUES (%s)"
            self.db_manager.cursor.execute(query, (quote_id,))
            self.db_manager.connection.commit()
            return True
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
