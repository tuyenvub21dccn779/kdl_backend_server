import pandas as pd
import json

from dao import process_query

def multiindex_to_grouped_json(df, value_columns):
    """
    Convert a DataFrame with MultiIndex into a nested JSON structure.

    Parameters:
    - df: A pandas DataFrame with a MultiIndex.
    - value_columns: A list of column names to aggregate (e.g., ["So Luong Dat", "Tong Tien"]).

    Returns:
    - A nested dictionary in JSON-like format.
    """

    def recursive_group(level, df_sub, index_names):

        grouped = []
        for key, group in df_sub.groupby(level=level):
            node = {
                index_names[level]: key,
                **{
                    col: float(group[col].sum())
                    for col in value_columns
                }
            }
            if level + 1 < len(index_names):
                node["children"] = recursive_group(level + 1, group, index_names)
            grouped.append(node)
        return grouped

    index_names = df.index.names
    totals = {
        index_names[0]: "All",
        **{
            col: float(df[col].sum())
            for col in value_columns
        },
        "children": recursive_group(0, df, index_names)
    }

    return totals

def create_query(
    dim: str,
    measures: list[str],
    attributes: list[str] | None,
    where: str | None = None
    ) -> str:
    col = "{ " + ", ".join([f"[Measures].[%s]" % x for x in measures]) + " } ON COLUMNS, \n"
    row = "NON EMPTY ("
    row = row + '\n * '.join([ f"[Dim %s].[%s].[%s]" % (dim, x, x) for x in attributes]) 
    row = row + ") ON ROWS "
    query = "SELECT " + col + row + "\nFROM [Kho Du Lieu]"
    return query


def get_sales_by_one_dimention(
    dimention: str
    ) -> dict:
    measures = ['So Luong Dat', 'Tong Tien']
    if dimention in ['khachhang', 'mathang', 'thoigian']:
        if dimention == 'mathang':
            index = ['Kich Thuoc', 'Mo Ta']
            query = create_query('Mat Hang', measures, index)
            
        elif dimention == 'khachhang':
            index = ['Bang', 'Ten Thanh Pho', 'Ten Khach Hang']
            query = create_query('Khach Hang', measures, index)
        else:
            index = ['Nam', 'Quy', 'Thang', 'Ngay']
            query = create_query('Thoi Gian', measures, index)
        data = process_query(query)
        data.set_index(index, inplace=True)
        result = multiindex_to_grouped_json(data, measures)
        return result
    return None
        