from flask import Blueprint
from flask_restplus import Api
from .test2_api import api as test2_api

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(
    blueprint,
    title='Test 2',
    version='1.0',
    description='DEMO API'
)

api.add_namespace(test2_api)
