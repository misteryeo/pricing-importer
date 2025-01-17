import pandas as pd
from sqlalchemy import create_engine, text

# Adjust pandas display settings
pd.set_option('display.max_columns', None)  # Show all columns

# Load the spreadsheet
file_path = 'pricing-spreadsheet.xlsx'  # Path to your spreadsheet
sheet_name = 'Sheet1'  # Specify the sheet name or index
data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# Clean column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')

# Split up key features into separate columns
# Specify the column to split
column_to_split = "key_features" 

# Split the column based on the delimiter and create new columns
split_columns = data[column_to_split].str.split(",", expand=True)

# Rename the new columns
split_columns.columns = [f"{column_to_split}_{i+1}" for i in range(split_columns.shape[1])]
data = pd.concat([data, split_columns], axis=1)

# Save the updated DataFrame back to a new file
output_file_path = "updated-pricing-spreadsheet.xlsx"
data.to_excel(output_file_path, index=False)

print(f"Updated spreadsheet saved to: {output_file_path}")

# Split into products and pricing tables
products = data[['plan_name', 'key_features_1', 'key_features_2', 'key_features_3', 'add-ons', 'support_level' ]].drop_duplicates()
pricing = data[['monthly_price_(usd)', 'annual_price_(usd)', 'usage_limits']]

# Create a database engine (SQLite in this case)
engine = create_engine('sqlite:///pricing_data.db')

# Write data to database
products.to_sql('products', engine, index=False, if_exists='replace')
pricing.to_sql('pricing', engine, index=False, if_exists='replace')

print("Data inserted into the database successfully!")

# Query data from the database
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM products LIMIT 5"))
    for row in result:
        print(row)
