import os
from dotenv import load_dotenv

# Cargar el archivo .env desde el directorio env/
load_dotenv(dotenv_path="env/.env")

# Acceder a las variables
api_token = os.getenv("API_TOKEN")
sql_server = os.getenv("SQL_SERVER")
sql_database = os.getenv("SQL_DATABASE")
sql_user = os.getenv("SQL_USER")
sql_password = os.getenv("SQL_PASSWORD")
driver = os.getenv("DRIVER")

print(f"Conectando a {sql_server} con la base de datos {sql_database}...")
