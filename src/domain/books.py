from .users import USER_ROLES

books = {
    'item_title': 'book',
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
    'allowed_roles': ['admin'],
    'allowed_read_roles': USER_ROLES,
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
        }
    }
}

categories = {
    'item_title': 'category',
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
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

borrows = {
    'item_title': 'borrow',
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "DELETE"],
    'allowed_roles': ['admin'],
    'allowed_read_roles': USER_ROLES,
    'schema': {
        'book': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'books'
            }
        },
        'reader': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'users'
            }
        }
    }
}
