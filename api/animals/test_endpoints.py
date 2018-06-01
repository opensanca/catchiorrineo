from datetime import datetime
import json
from flask import url_for
from api.common.utils import HTTP_STATUS_CODES
from .model import Animal


def test_animals(client):
    animal = Animal(name='Dog 1',
                    age=64,
                    breed=['lontras'],
                    arrived_date=datetime(2018, 1, 1),
                    description="um cachorro do barulho")
    animal.save()
    response = client.get(url_for('animal.animals'))
    assert response.status_code == HTTP_STATUS_CODES['OK']
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['id'] == str(animal.id)


def test_create_animal(client):
    headers = {
        'Content-Type': 'application/json',
    }
    data = json.dumps({
        'name': 'Doguito',
        'age': '2',
        'breed': ['SRD'],
        'description': 'Doguito preto e branco',
        'arrived_date': '2018-01-21',
    })
    response = client.post(url_for('animal.create_animal'), data=data, headers=headers)
    assert response.status_code == HTTP_STATUS_CODES['OK']


def test_update_animal(client):
    animal = Animal(name='Dog 2',
                    age=5,
                    breed=['unicornio', 'cachorro'],
                    arrived_date=datetime(2018, 1, 10),
                    description="um unicornio do barulho")

    animal.save()
    mock_data = json.dumps({
        'name': 'Dog 2 editado',
        'age': '6',
        'breed': ['unicornio', 'lontra'],
        'description': 'unicornio preto e branco',
        'arrived_date': '2018-01-10',
    })
    headers = {
        'Content-Type': 'application/json',
    }
    params = {'animal_id': animal.id}
    response = client.put(url_for('animal.update_animal', **params),
                          data=mock_data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == HTTP_STATUS_CODES['OK']
    assert data == str(animal.id)

    animal_updated = Animal.objects.get(id=animal.id)
    assert animal_updated.name == 'Dog 2 editado'
    assert animal_updated.breed == ['unicornio', 'lontra']


def test_delete_animal(client):
    animal = Animal(name='Dog 2',
                    age=5,
                    breed=['unicornio', 'cachorro'],
                    arrived_date=datetime(2018, 1, 10),
                    description="um unicornio do barulho")

    animal.save()
    params = {'animal_id': animal.id}
    response = client.delete(url_for('animal.delete_animal', **params))

    assert response.status_code == HTTP_STATUS_CODES['OK']
    assert not Animal.objects.filter(id=animal.id).count()
