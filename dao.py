from sys import path
from pandas import DataFrame


path.append('C:\\Program Files\\Microsoft.NET\\ADOMD.NET\\160')

from pyadomd import Pyadomd

conn_str = 'Provider=MSOLAP;Data Source=localhost;Catalog=kho_du_lieu;'

def process_columns_name(name: str) -> str:
    arr = name.split(".")
    if "[Measures]" in arr:
        return arr[-1][1:-1]
    else:
        return arr[-2][1:-1]

def process_query(query: str) -> DataFrame:
    with Pyadomd(conn_str) as conn:
        with conn.cursor().execute(query) as cur:
            df = DataFrame(cur.fetchone(),
            columns=[process_columns_name(i.name) for i in cur.description])
            
            return df
