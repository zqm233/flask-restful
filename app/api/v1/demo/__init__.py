from app.api.v1.demo.views import DemoView
from app.api.v1.demo.views import TestView


def init(api):
    api.add_resource(DemoView, '/demo')
    api.add_resource(TestView, '/test')
