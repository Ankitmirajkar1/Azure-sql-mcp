## Read the schema information dynamically from the database

import pandas as pd
from app.database.connection import engine ## Import the SQLAlchemy engine from the connection module

def describe_table(table_name: str):
    query = f"""
    SELECT 
        COLUMN_NAME, 
        DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = '{table_name}'
    """
    df = pd.read_sql(query, engine) ## Use the SQLAlchemy engine to execute the query and read the results into a DataFrame

    return df.to_dict(orient='records') ## Convert the DataFrame to a list of dictionaries for easier handling in the application