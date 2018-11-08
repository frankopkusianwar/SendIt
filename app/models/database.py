import uuid

class User:

    def __init__(self, name='', email='', password='', user_type='user', user_id = str(uuid.uuid4())):
        self.name = name
        self.user_type = user_type
        self.email = email
        self.password = password
        self.user_id = user_id


userList = [

    {
    'user_id': str(uuid.uuid4()),
    'name': 'Okiror frank',
    'email': 'okirorfrank3@gmail.com',
    'password': '12345',
    'user_type': 'user'
    }
]

class Parcel:

    weight = 0
    contact=''

    def __init__(self, pick_up_location='', destination='', parcel_id = str(uuid.uuid4())):
        self.pick_up_location = pick_up_location
        self.destination = destination
        self.parcel_id = str(uuid.uuid4())

ParcelList = [
    {
    'parcel_id': str(uuid.uuid4()),
    'pick_up_location': 'Entebe',
    'destination': 'kampala',
    'contact': '0781564622',
    'wight': 30
    }
]


