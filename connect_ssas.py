from sys import path
import pandas as pd
import json

path.append('C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')

from pyadomd import Pyadomd

conn_str = 'Provider=MSOLAP;Data Source=localhost;Catalog=kho_du_lieu;'

query = """
SELECT NON EMPTY ([Dim Khach Hang].[Bang].[Bang] 
* [Dim Khach Hang].[Ten Thanh Pho].[Ten Thanh Pho]) ON COLUMNS,
NON EMPTY ([Dim Mat Hang].[Kich Thuoc].[Kich Thuoc] * [Dim Mat Hang].[Mo Ta].[Mo Ta]) ON ROWS
FROM [Kho Du Lieu]
"""

def process_columns_name(name: str) -> str:
    arr = name.split(".")
    if "[Measures]" in arr:
        return arr[-1][1:-1]
    else:
        return arr[-2][1:-1]

with Pyadomd(conn_str) as conn:
    with conn.cursor().execute(query) as cur:
        df = pd.DataFrame(cur.fetchall())
        print(df)