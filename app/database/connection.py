## Create SQLAlchemy engine for Azure SQL Database connection

from sqlalchemy import create_engine
from app.config.settings import settings
from urllib.parse import quote_plus

# Construct the parameters for the connection string
odbc_connection_string = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};" # Adjust the driver name if needed
    f"SERVER={settings.SQL_SERVER};" # Adjust the server key if needed
    f"DATABASE={settings.SQL_DATABASE};" # Adjust the database key if needed
    f"UID={settings.SQL_USERNAME};" # Adjust the username key if needed
    f"PWD={settings.SQL_PASSWORD};" # Adjust the password key if needed
    f"Encrypt=yes;" # Adjust based on your security requirements
    f"TrustServerCertificate=no;" # Adjust based on your security requirements
    f"Connection Timeout=30;"   # Adjust the timeout as needed
)
params = quote_plus(odbc_connection_string)

# Create the SQLAlchemy engine using the connection string
connection_string = f"mssql+pyodbc:///?odbc_connect={params}" ## Use the correct driver name for your system

## Database engine
engine = create_engine(connection_string) ## Create the SQLAlchemy engine using the connection string
