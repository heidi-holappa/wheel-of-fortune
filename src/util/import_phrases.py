import os

from util.database_connection import get_database_connection
from util.config import DATA_PATH


def import_phrases(filename: str):
    """Imports phrases from a file to the database

    Args:
        file_name (str): a name of the file to be imported.
    """
    connection = get_database_connection()
    cursor = connection.cursor()

    file_path = os.path.join(DATA_PATH, filename)

    with open(file_path, 'r') as file:
        for line in file:
            line = line.rstrip("\n")
            line = line.split(";")
            cursor.execute('''
                INSERT INTO PHRASES (phrase, author, source, category)
                VALUES (?, ?, ?, ?)
            ''', (line[0], line[1], line[2], line[3]))
            connection.commit()
