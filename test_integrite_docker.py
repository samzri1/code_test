import pytest
import requests
import pandas as pd
import psycopg2

@pytest.fixture(scope='module')
def database():
    # Connexion à la base de données
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='test_db',
        user='test_user',
        password='test_password'
    )
    data = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    data.to_sql('users', con=connection)
    print('Base de données initialisée avec succès')
    yield
    # Fermeture de la connexion
    connection.close()
    print('Connexion à la base de données fermée')

@pytest.fixture(scope='module')
def service(database):
    # Connexion au service web
    url = 'http://localhost:5000/users'
    print('Connexion au service web établie')
    yield url
    # Fermeture de la connexion
    print('Connexion au service web fermée')

def test_get_users(service):
    # Test de la récupération des utilisateurs via le service web
    print('Test de la récupération des utilisateurs via le service web...')
    response = requests.get(service)
    assert response.status_code == 200
    assert len(response.json()) == 3
    print('Test réussi : la réponse contient bien les trois utilisateurs')

def test_add_user(database, service):
    # Test de l'ajout d'un utilisateur via le service web
    print('Test de l\'ajout d\'un utilisateur via le service web...')
    data = {'id': 4, 'name': 'David'}
    response = requests.post(service, json=data)
    assert response.status_code == 201

    # Vérification que l'utilisateur a bien été ajouté à la base de données
    connection = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='test_db',
        user='test_user',
        password='test_password'
    )
    data = pd.read_sql_query('SELECT * FROM users WHERE id = 4', con=connection)
    assert len(data) == 1
    connection.close()
    print('Test réussi : l\'utilisateur a bien été ajouté à la base de données')
