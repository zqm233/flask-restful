from common.grpc.demo import demo_pb2, demo_pb2_grpc
import grpc
from common.utils import MessageToDict
from common.discovery import get_service_stub


class DemoHelper:

    def demo_client(self, params):
        stub = get_service_stub('demo_service', demo_pb2_grpc.DemoServiceStub)
        req = demo_pb2.RequestData(
            data=params
        )
        response = stub.call_rpc('CreateOne', req)
        return MessageToDict(response, including_default_value_fields=True,
                             preserving_proto_field_name=True)
