import customtkinter as ctk
import os

from dotenv import load_dotenv

# Database imports
from Database.database_manager import DatabaseManager
from Database.invoicing_db import InvoiceDatabase

# GUI imports

# Security Imports
from Security.user_authentication import UserAuthentication

load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")


def main():
    app = ctk.CTk()
    db_manager = DatabaseManager(db_name, db_user, db_password, db_host, db_port)
    user_auth = UserAuthentication(db_manager)

    app.mainloop()


if __name__ == "__main__":
    main()
