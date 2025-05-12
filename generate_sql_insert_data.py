# Generate SQL INSERT statements for each table and export to a single .sql file
import pandas as pd

# Load all CSV files
files = {
    "DimThoiGian": "data/DimThoiGian.csv",
    "DimThanhPho": "data/DimThanhPho.csv",
    "DimCuaHang": "data/DimCuaHang.csv",
    "DimKhachHang": "data/DimKhachHang.csv",
    "DimMatHang": "data/DimMatHang.csv",
    "FactSales": "data/FactSales.csv",
    "FactInventory": "data/FactInventory.csv",
}

# Retry with encoding override
dfs = {name: pd.read_csv(path, encoding='latin1') for name, path in files.items()}


def generate_insert_statements(df, table_name):
    statements = []
    for _, row in df.iterrows():
        values = []
        for value in row:
            if pd.isna(value):
                values.append("NULL")
            elif isinstance(value, str):
                escaped = value.replace("'", "''")
                values.append(f"'{escaped}'")
            else:
                values.append(str(value))
        values_str = ", ".join(values)
        statements.append(f"INSERT INTO {table_name} VALUES ({values_str});")
    return statements

# Generate SQL script
sql_statements = []
for table_name, df in dfs.items():
    sql_statements.extend(generate_insert_statements(df, table_name))

# Write all statements to a .sql file
sql_file_path = "data/Insert_Data_Warehouse.sql"
with open(sql_file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(sql_statements))

