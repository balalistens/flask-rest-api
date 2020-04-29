"""
Defines the blueprint for the post
"""
from flask import Blueprint
from flask_restful import Api

from resources import PostResource

POST_BLUEPRINT = Blueprint("post", __name__)
Api(POST_BLUEPRINT).add_resource(PostResource, "/posts")
