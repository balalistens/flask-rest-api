from flask import jsonify


class APIError(Exception):
    """Common base class for all API errors
    """

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv["message"] = self.message
        return rv


def handle_error(error):
    response = jsonify({"message": "Internal Server Error"})
    response.status_code = 500
    return response


def handle_api_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def register_custom_error_handlers(app):
    """Register custom error handlers

    :param app: Flask App
    :type app: flask
    """

    app.register_error_handler(Exception, handle_error)
    app.register_error_handler(APIError, handle_api_error)
