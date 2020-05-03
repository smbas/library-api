from eve import Eve
from flask import jsonify, request, abort
from auth import LibraryAuth
from auth import create_token, get_user_by_token, get_user_by_login_data, update_user_token
from auth import on_insert_users
from datetime import timedelta
from utils import get_request_param


app = Eve(auth=LibraryAuth)
app.on_insert_users += on_insert_users


@app.route('/login', methods=['POST'])
def login():
    email = get_request_param(request, 'email')
    if not email:
        abort(400, description="Missing email parameter")

    password = get_request_param(request, 'password')
    if not password:
        abort(400, description="Missing password parameter")

    user = get_user_by_login_data(email, password)
    if not user:
        abort(404, description="No such user")

    user_id = str(user['_id'])
    expiration = timedelta(days=1)
    token = create_token(user_id, expiration)
    update_user_token(user, token)
    return jsonify({'token': token})


@app.route('/logout', methods=['POST'])
def logout():
    token = get_request_param(request, 'Authorization')
    if not token:
        abort(401, description="Please provide proper credentials")

    user = get_user_by_token(token)
    if not user:
        abort(404, description="No such user")

    update_user_token(user, "")
    return ""


if __name__ == "__main__":
    app.run(host='0.0.0.0')
