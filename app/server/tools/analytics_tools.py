### Contains business analytics logic and functions to process data for analytics purposes. This may include data aggregation, transformation, and visualization logic specific to the application's analytics features.

import pandas as pd

from app.database.connection import engine ## Import the SQLAlchemy engine from the connection module

## Top customers by revenue
def top_customer():
    query = """
    SELECT TOP 10 
        CustomerID, 
        SUM(TotalDue) AS TotalRevenue
    FROM SalesLT.SalesOrderHeader
    GROUP BY CustomerID
    ORDER BY TotalRevenue DESC
    """
    df = pd.read_sql(query, engine) ## Use the SQLAlchemy engine to execute the query and read the results into a DataFrame

    return df.to_dict(orient='records') ## Convert the DataFrame to a list of dictionaries for easier handling in the application

## from SalesLT.SalesOrderHeader, get the total revenue by year
def revenue_by_year():
    query = """
    SELECT 
        YEAR(OrderDate) AS OrderYear, 
        SUM(TotalDue) AS TotalRevenue
    FROM SalesLT.SalesOrderHeader
    GROUP BY YEAR(OrderDate)
    ORDER BY OrderYear
    """
    df = pd.read_sql(query, engine) ## Use the SQLAlchemy engine to execute the query and read the results into a DataFrame

    return df.to_dict(orient='records') ## Convert the DataFrame to a list of dictionaries for easier handling in the application