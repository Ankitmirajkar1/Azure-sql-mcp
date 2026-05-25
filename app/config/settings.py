from dotenv import load_dotenv
import os
from pathlib import Path

## get base directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent # Adjust the number of .parent as needed to reach the root of your project

## Build the path to the .env file
ENV_PATH = BASE_DIR / '.env'

## Load environment variables from the .env file
load_dotenv(ENV_PATH)

## Access environment variables

class Settings:
    ## Groq API Key & Azure SQL Database credentials
    GROQ_API_KEY=os.getenv('GROQ_API_KEY')
    SQL_SERVER=os.getenv('AZURE_SQL_SERVER')
    SQL_DATABASE=os.getenv('AZURE_SQL_DATABASE')
    SQL_USERNAME=os.getenv('AZURE_SQL_USERNAME')
    SQL_PASSWORD=os.getenv('AZURE_SQL_PASSWORD')

settings = Settings()