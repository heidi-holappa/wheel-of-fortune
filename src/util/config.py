import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.db'
DATA_PATH = os.path.join(dirname, '..', 'data')
DATABASE_FILE_PATH = os.path.join(DATA_PATH, DATABASE_FILENAME)

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)
