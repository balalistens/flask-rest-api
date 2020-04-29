"""
Define the REST verbs relative to the comments
"""
import requests
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from config import JSON_API_URL
from util import parse_params
from util.error_handlers import APIError


class CommentResource(Resource):
    """ Verbs relative to the comments """

    @staticmethod
    def get():
        """ Return a list of comments """

        try:
            r = requests.get(JSON_API_URL + "/comments")
            comments = r.json()

            return jsonify({"comments": comments})
        except requests.exceptions.RequestException:
            raise APIError("JSON Placeholder Service Unavailable", 503)
