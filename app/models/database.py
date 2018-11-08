import uuid

class User(object):

    def __init__(self, name='', email='', password='', user_type='user', id = str(uuid.uuid4())):
        self.name = name
        self.user_type = user_type
        self.email = email
        self.password = password
        self.id = id


userList = [

    {
    'id': str(uuid.uuid4()),
    'name': 'Okiror frank',
    'email': 'okirorfrank3@gmail.com',
    'password': '12345',
    'user_type': 'user'
    }
]