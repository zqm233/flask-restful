from common.grpc.demo import demo_pb2, demo_pb2_grpc
import grpc
from common.utils import MessageToDict


class DemoHelper:

    def demo_client(self, params):
        with grpc.insecure_channel('localhost:50002') as channel:
            stub = demo_pb2_grpc.DemoServiceStub(channel)
            req = demo_pb2.RequestData(
                data=params
            )
            response = stub.CreateOne(req)
            return MessageToDict(response, including_default_value_fields=True,
                                 preserving_proto_field_name=True)
