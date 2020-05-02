books = {
    'item_title': 'book',
    "resource_methods": ["GET", "POST"],
    "item_methods": ["GET", "PATCH", "DELETE"],
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
    'schema': {
        'name': {
            'type': 'string',
            'empty': False,
            'unique': True,
            'required': True
        }
    }
}
