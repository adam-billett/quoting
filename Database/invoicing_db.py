from Database import database_manager
import psycopg2


class InvoiceDatabase:
    def __int__(self, db_manager):
        self.db_manager = db_manager

    def get_invoice_id(self, company_name):
        try:
            query = "SELECT quote_id FROM quotes WHERE company_name = %s"
            self.db_manager.connection.execute(query, company_name)
            result = self.db_manager.cursor.fetchone()

            if result:
                return True
            else:
                return None

        except Exception as e:
            print(f"Error: {e}")
