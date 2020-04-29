"""
Define the REST verbs relative to the posts
"""
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from util import parse_params


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
        posts = {"hello": "world"}

        return jsonify({"posts": posts})
