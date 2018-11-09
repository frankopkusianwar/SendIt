from flask import json
import pytest
from app.models.database import Parcel, ParcelList
from app import app

@pytest.fixture
def client(request):
    app.config['TESTING'] = True
    client = app.test_client()
    return client


def json_response(response):
    resp =  json.loads(response.data.decode('utf8'))
    return [resp]

def test_create_parcel_delivery_order(client):
    parcel = Parcel('kampala', 'jinja')
    with client:
        parcel.weight = 20
        parcel.contact = '0781564622'
        resp = client.post('api/v1/parcels', data = json.dumps(dict(
            parcel_id = parcel.parcel_id,
            pick_up_location = parcel.pick_up_location,
            destination = parcel.destination,
            contact = parcel.contact,
            weight = parcel.weight

        )) , content_type ='application/json')
        parcel_data = {
        'patcel_id': parcel.parcel_id,
        'pick_up_location': parcel.pick_up_location,
        'destination': parcel.destination,
        'contact': parcel.contact,
        'weight': parcel.weight
        }
        ParcelList.append(parcel_data)
        assert resp.status_code == 201
        
            
