from .users import users, admins, readers
from .books import books, categories, borrows

DOMAIN = {
    'users': users,
    'admins': admins,
    'readers': readers,
    'books': books,
    'categories': categories,
    'borrows': borrows
}
