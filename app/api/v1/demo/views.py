from flask_restful import Resource
from app.api.v1.demo.helps import DemoHelper
from flask import request


class DemoView(Resource):

    def get(self):
        result = DemoHelper().demo_client(request.args['data'])
        return result


class TestView(Resource):
    def get(self):
        return request.args['name']
