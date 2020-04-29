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
            posts_dict = {}

            r = requests.get(JSON_API_URL + "/posts")
            posts_list = r.json()

            r = requests.get(JSON_API_URL + "/comments")
            comments = r.json()

            # dict/list comprehension is the fastest way to iterate - O(n)
            posts_dict = {
                post["id"]: dict(post, **{"commentsCount": 0}) for post in posts_list
            }

            # O(n)
            for comment in comments:
                if comment["postId"] in posts_dict and comment["postId"]:
                    posts_dict[comment["postId"]]["commentsCount"] += 1

            # O(n)
            posts_list = [post for post in posts_dict.values()]

            # sorted: worstcase: O(n log n) - provided the key function is O(1)
            posts_list = sorted(
                posts_list, key=lambda post: post["commentsCount"], reverse=True
            )

            if top and top < len(posts_list):
                posts_list = posts_list[:top]

            return jsonify({"posts": posts_list})
        except requests.exceptions.RequestException:
            raise APIError("JSON Placeholder Service Unavailable", 503)
