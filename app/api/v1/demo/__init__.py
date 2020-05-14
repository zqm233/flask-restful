from views import DemoView
from views import TestView


def init(api):
    api.add_resource(DemoView, '/demo')
    api.add_resource(TestView, '/test')
