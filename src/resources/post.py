"""
Define the REST verbs relative to the posts
"""
import requests
from flask import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from config import JSON_API_URL
from util import parse_params
from util.error_handlers import APIError


class PostResource(Resource):
    """ Verbs relative to the post """

    @staticmethod
    @parse_params(
        Argument(
            "top",
            type=int,
            location="args",
            required=False,
            help="`top` posts based on the number of comments",
        )
    )
    def get(top):
        """ Return a list of top posts based on the number of comments """

        try:
            r = requests.get(JSON_API_URL + "/posts")
            return jsonify({"posts": r.json()})
        except requests.exceptions.RequestException:
            raise APIError("JSON Placeholder Service Unavailable", 503)
