"""
Defines the blueprint for the comment
"""
from flask import Blueprint
from flask_restful import Api

from resources import CommentResource

COMMENT_BLUEPRINT = Blueprint("comment", __name__)
Api(COMMENT_BLUEPRINT).add_resource(CommentResource, "/comments")
