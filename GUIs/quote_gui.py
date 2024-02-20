# gui for when the user clicks the search for quotes
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from Database.quoting_db import QuoteDatabase


class Quotegui:

    def __init__(self, app, db_manager, gui_manager):
        self.app = app
        self.db_manager = db_manager
        self.quoting_db = QuoteDatabase(self.db_manager)
        self.gui_manager = gui_manager

    def search_menu(self):

        self.app.withdraw()

        self.create_search_frame = ctk.CTkToplevel(self.app)
        self.create_search_frame.geometry("500x500")
        self.create_search_frame.title("Search")
        self.create_search_frame.protocol("WM_DELETE_WINDOW", self.gui_manager.on_close)

        self.id_entry = ctk.CTkEntry(self.create_search_frame, placeholder_text="Quote ID")
        self.id_entry.pack(pady=8, padx=8)

        self.company_entry = ctk.CTkEntry(self.create_search_frame, placeholder_text="Company")
        self.company_entry.pack(pady=8, padx=4)

        self.date_entry = ctk.CTkEntry(self.create_search_frame, placeholder_text="Date")
        self.date_entry.pack(pady=8, padx=4)

        self.search_btn = ctk.CTkButton(self.create_search_frame, command=lambda: self.search_quote,
                                        text="Search")
        self.search_btn.pack(pady=8, padx=4)

        self.quote_lbl = ctk.CTkLabel(self.create_search_frame)
        self.quote_lbl.pack(pady=8, padx=4)

    def search_quote(self):
        if self.id_entry.get():
            self.display_quote(self.id_entry.get())
        elif self.company_entry.get():
            self.display_quote()
        elif self.date_entry.get():
            self.display_quote()
        else:
            self.display_all_quotes()

    def display_quote(self, quote_id):
        quote = self.quoting_db.get_quote(quote_id)

        for company, date in quote:
            quote_txt = (company, date)

        self.quote_lbl.configure(text=quote_txt)
        self.quote_txt = quote_txt

    def display_all_quotes(self):
        quotes = self.quoting_db.get_quotes()

        for company, date in quotes:
            quote_txt = (company, date)

        self.quote_lbl.configure(text=quote_txt)
        self.quote_txt = quote_txt
