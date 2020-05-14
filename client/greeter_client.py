from common.grpc.greeter import helloworld_pb2_grpc, helloworld_pb2
import grpc


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='zqm'))
    print('Greeter client received: '+response.message)


if __name__ == '__main__':
    run()
