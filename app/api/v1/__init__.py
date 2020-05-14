from flask_restful import Api
from app.api.v1 import demo
api = Api(prefix='/zqm/v1')


def init(app):
    demo.init(api)
    api.init_app(app)
