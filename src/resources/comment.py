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
from util.helpers import filter_comments


class CommentResource(Resource):
    """ Verbs relative to the comments """

    @staticmethod
    @parse_params(
        Argument(
            "body",
            type=str,
            location="args",
            required=False,
            help="`body` filter comments based on the provided string",
        ),
        Argument(
            "name",
            type=str,
            location="args",
            required=False,
            help="`name` filter comments based on the provided string",
        ),
        Argument(
            "email",
            type=str,
            location="args",
            required=False,
            help="`email` filter comments based on the provided string",
        ),
        Argument(
            "id",
            type=int,
            location="args",
            required=False,
            help="`id` filter comments based on the provided id",
        ),
        Argument(
            "postId",
            type=int,
            location="args",
            required=False,
            help="`postId` filter comments based on the provided id",
        ),
    )
    def get(**kwargs):
        """ Return a list of comments """

        try:
            r = requests.get(JSON_API_URL + "/comments")
            comments = r.json()

            # list comprehension with condition is the fastest way to filter - O(n)
            comments = [v for v in comments if filter_comments(v, kwargs)]

            return jsonify({"comments": comments})
        except requests.exceptions.RequestException:
            raise APIError("JSON Placeholder Service Unavailable", 503)
