# Pricing and Packaging Data Extractor

This project is a Python-based tool designed to extract pricing and packaging data from Excel spreadsheets, clean and normalize it, and prepare it for insertion into a database. It simplifies data preparation for analysis or integration into larger systems.

---

## Features
- Reads pricing and packaging data from `.xlsx` files.
- Cleans and normalizes column names and data formats.
- Handles missing values and ensures database-ready formatting.
- Supports multiple database systems using SQLAlchemy or SQLite.
- Modular design for easy expansion or customization.

---

## Requirements

### Python Version
- Python 3.8 or higher

### Dependencies
Install the required libraries by running:
```bash
pip install -r requirements.txt
```

Required libraries:
- `pandas`
- `openpyxl`
- `SQLAlchemy`

---

## Usage

### 1. Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/misteryeo/pricing-importer.git
   cd pricing-importer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your input file (e.g., `pricing-spreadsheet.xlsx`) has been included in your repo.

### 2. Run the Script
Execute the main script to extract and process the data:
```bash
python src/main.py
```

### 3. Output
- The script will generate a cleaned database-ready output (e.g., `pricing_data.db`).

---

## Contact
For questions or support, please contact:
- **Email**: [andy.yeo@gmail.com](mailto:andy.yeo@gmail.com)
- **GitHub**: [misteryeo](https://github.com/misteryeo)

