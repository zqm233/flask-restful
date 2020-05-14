import grpc
from common.grpc.demo import demo_pb2, demo_pb2_grpc


def run():

    with grpc.insecure_channel('localhost:50002') as channel:
        stub = demo_pb2_grpc.DemoServiceStub(channel)
        req = demo_pb2.RequestData(
            data='call CreateOne from client'
        )
        response = stub.CreateOne(req)
        print(response.return_code, response.message, response.data)


if __name__ == '__main__':
    run()
