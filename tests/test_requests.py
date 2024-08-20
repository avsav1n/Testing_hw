import pytest
import sys
import os
sys.path.append(os.getcwd())

import requests

import main


URL = 'https://cloud-api.yandex.net/v1/disk/resources'
PARAMS = {'path': 'Folder for testing'}
HEADERS = {'Authorization': f'OAuth {os.getenv('YADISKTOKEN')}'}

@pytest.fixture(scope='module')
def delete_folder():
    requests.delete(URL, params=PARAMS, headers=HEADERS)

def test_create_yadisk_folder_code_404(delete_folder):
    '''Проверка на отсутствие папки на ЯДиске
    '''
    response = requests.get(URL, params=PARAMS, headers=HEADERS)
    assert response.status_code == 404

def test_create_yadisk_folder_code_201(delete_folder):
    '''Тест функции create_yadisk_folder
       Создание папки на ЯДиске
    '''
    response = main.create_yadisk_folder()
    assert response.status_code == 201

def test_create_yadisk_folder_code_200():
    '''Проверка на существование папки на ЯДиске
    '''
    response = requests.get(URL, params=PARAMS, headers=HEADERS)
    assert response.status_code == 200

def test_create_yadisk_folder_code_409():
    '''Тест функции create_yadisk_folder
       Попытка создания еще одной папки поверх существующей
    '''
    response = main.create_yadisk_folder()
    assert response.status_code == 409
