import pandas as pd

# Load the spreadsheet
file_path = 'pricing-spreadsheet.xlsx'  # Path to your spreadsheet
sheet_name = 'Sheet1'  # Specify the sheet name or index
data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# Preview the data
print(data.head())
