import pandas as pd
import pytest
import sqlite3

connection = sqlite3.connect(':memory:')

@pytest.fixture
def database():
    # Connexion à la base de données
    data = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    data.to_sql('users', con=connection)
    yield
    # Fermeture de la connexion

def test_database(database):
    # Test de la connexion à la base de données
    data = pd.read_sql_query('SELECT * FROM users', con=connection)
    print(data)
    assert len(data) == 4, "Error: Number of users in database is not 3"
    print("Test passed: Number of users in database is 3")
if __name__ == '__main__':
    pytest.main([__file__])


# pytest .\test_integrite.py  