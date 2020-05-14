from common.grpc.demo import demo_pb2, demo_pb2_grpc
import grpc
from concurrent import futures
from common.logger import log


class DemoServicer(demo_pb2_grpc.DemoServiceServicer):

    @log
    def CreateOne(self, request, context):
        return demo_pb2.ResponseData(return_code=200, message='create one ', data='1234')

    def DeleteOne(self, request, context):
        return demo_pb2.ResponseData(return_code=200, message='delete one ', data='1234')

    def TransferOne(self, request, context):
        return demo_pb2.ResponseData(return_code=200, message='transfer one ', data='1234')

    def GetCreateNotify(self, request, context):
        return demo_pb2.ResponseData(return_code=200, message='GetCreateNotify one ', data='1234')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))
    demo_pb2_grpc.add_DemoServiceServicer_to_server(DemoServicer(), server)
    server.add_insecure_port('[::]:50002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
