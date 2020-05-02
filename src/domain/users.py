USER_ROLES = ['admin', 'reader']

users = {
    'item_title': 'user',
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    'schema': {
        'email': {
            'type': 'string',
            'regex': '[^@]+@[^@]+\.[^@]+',
            'empty': False,
            'unique': True,
            'required': True
        },
        'password': {
            'type': 'string',
            'minlength': 8,
            'required': True
        },
        'role': {
            'type': 'string',
            'allowed': USER_ROLES,
            'required': True
        }
    }
}

admins = {
    'datasource': {
        'item_title': 'admin',
        'source': 'users',
        'filter': {
            'role': 'admin'
        }
    }
}

readers = {
    'datasource': {
        'item_title': 'admin',
        'source': 'users',
        'filter': {
            'role': 'reader'
        }
    }
}
