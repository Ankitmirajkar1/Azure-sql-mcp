## To provide the resusable code for executing queries

import pandas as pd
from sqlalchemy import text
from app.database.connection import engine ## Import the SQLAlchemy engine from the connection module

## Function to get all the tables in the database
def list_tables():
    query = """
    SELECT TABLE_NAME
    FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_TYPE = 'BASE TABLE'
    """
    df = pd.read_sql(query, engine) ## Use the SQLAlchemy engine to execute the query and read the results into a DataFrame

    return df.to_dict(orient='records') ## Convert the DataFrame to a list of dictionaries for easier handling in the application

## Function to execute custom SQL query
def execute_sql_query(query: str):  ## Define a function that takes a SQL query as input
    with engine.connect() as conn:
        result = conn.execute(text(query)) ## Use the SQLAlchemy engine to execute the provided query
        
        rows = [dict(row._mapping) for row in result] ## Convert the result to a list of dictionaries for easier handling in the application
    
    return rows