from .users import USER_ROLES

books = {
    'item_title': 'book',
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'allowed_roles': ['admin'],
    'allowed_read_roles': USER_ROLES,
    'versioning': True,
    'schema': {
        'title': {
            'type': 'string',
            'empty': False,
            'required': True
        },
        'author': {
            'type': 'string',
            'empty': False,
            'required': True
        },
        'categories': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'categories',
                    'embeddable': True
                }
            },
            'empty': False,
            'required': True,
        },
        'reader': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'readers'
            },
            'nullable': True
        }
    }
}

categories = {
    'item_title': 'category',
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET', 'PATCH', 'DELETE'],
    'allowed_roles': ['admin'],
    'allowed_read_roles': USER_ROLES,
    'schema': {
        'name': {
            'type': 'string',
            'empty': False,
            'unique': True,
            'required': True
        }
    }
}
