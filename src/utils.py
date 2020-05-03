def get_request_param(request, name):
    headers = request.headers
    if headers and name in headers:
        return headers[name]

    json = request.json
    if json and name in json:
        return json[name]

    values = request.values
    if values and name in values:
        return values[name]
    return None
