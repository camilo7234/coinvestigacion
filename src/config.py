import os
from dotenv import load_dotenv

load_dotenv()  # lee .env

# Configuración DB
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT', 5432))
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Configuración PStrace
PSTRACE_HOST = os.getenv('PSTRACE_HOST', 'localhost')
PSTRACE_PORT = int(os.getenv('PSTRACE_PORT', 5000))