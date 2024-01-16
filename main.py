# Application for sales reps to use to make a new quote, will generate an invoice number
import PyPDF2
import openpyxl

# Create a new excel workbook
workbook = openpyxl.Workbook()

# Select the active sheet
sheet = workbook.active

# Write data to the cells
sheet['A1'] = "Hello"
sheet['B1'] = "World!"

# Save the workbook to a file
workbook.save('example_2346.xlsx')

# Open up an existing workbook
existing_workbook = openpyxl.load_workbook('example.xlsx')

# Select a sheet in the active workbook
existing_sheet = existing_workbook.active

# Read data from the cells
value_a1 = existing_sheet['A1'].value
value_b1 = existing_sheet['B1'].value

print(f'Value in A1: {value_a1}')
print(f'Value in B1: {value_b1}')

# Application