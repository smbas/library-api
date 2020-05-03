from eve.auth import TokenAuth
from flask import current_app as app

from datetime import datetime

import jwt
import bcrypt


class LibraryAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        user = get_user_by_token(token)
        if not user:
            return False

        return verify_token(token, user, allowed_roles)


def create_token(user_id, expiration):
    payload = {
        'sub': user_id,
        'exp': datetime.utcnow() + expiration
    }

    token = jwt.encode(payload, 'secret').decode('unicode_escape')
    return token


def verify_token(token, user, allowed_roles):
    if not token:
        return False

    try:
        jwt.decode(token, 'secret')
    except jwt.InvalidTokenError:
        return False

    if allowed_roles and user['role'] not in allowed_roles:
        return False

    return True


def get_users():
    return app.data.driver.db['users']


def get_user_by_token(token):
    users = get_users()
    user = users.find_one({'token': token})
    return user


def get_user_by_login_data(email, password):
    users = get_users()
    user = users.find_one({'email': email})
    if not user:
        return None
    if not check_user_password(user, password):
        return None
    return user


def update_user_token(user, token):
    users = get_users()
    users.update({'_id': user['_id']}, {'$set': {'token': token}})


def protect_user_password(user):
    salt = bcrypt.gensalt()
    password = user['password'].encode('utf-8')
    hashed_password = bcrypt.hashpw(password, salt)
    user['password'] = hashed_password


def check_user_password(user, password):
    hashed_password = user['password']
    return hashed_password == bcrypt.hashpw(password.encode('utf-8'), hashed_password)


def on_insert_users(documents):
    for document in documents:
        protect_user_password(document)
