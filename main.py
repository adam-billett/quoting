# Application for sales reps to use to make a new quote, will generate an invoice number
import PyPDF2
import openpyxl
from datetime import date

today = date.today()
# Create a new Excel workbook
workbook = openpyxl.load_workbook('blank quote.xlsx')

# Select the active sheet
sheet = workbook.active

sheet['G4'] = 'Quote: 22586'
sheet['G6'] = f'Date: {today}'

workbook.save('New_quote.xlsx')

# Open up an existing workbook
existing_workbook = openpyxl.load_workbook('New_quote.xlsx')

# Select a sheet in the active workbook
existing_sheet = existing_workbook.active

# Read data from the cells
value_a1 = existing_sheet['A1'].value
value_b1 = existing_sheet['B1'].value

print(f'Value in A1: {value_a1}')
print(f'Value in B1: {value_b1}')

# Application